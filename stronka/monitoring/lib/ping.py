import sqlite3
import nmap
import datetime
import smtplib
from email.mime.text import MIMEText
import os
import sys

def error_email(message):
    msg = MIMEText(message, 'plain')

    me = 'awaria@wer.pl'
    you = 'karol.piszczek@gmail.com'
    msg['Subject'] = 'Awaria'
    msg['From'] = me
    msg['To'] = you
    s = smtplib.SMTP('localhost')
    s.sendmail(me, [you], msg.as_string())
    s.quit()

def ping():
    data_base = sqlite3.connect('db.sqlite3')
    c = data_base.cursor()
    c.execute('SELECT ip FROM monitoring_device')
    ip_list = c.fetchall()
    lista=''
    for i in ip_list:
        lista += i[0] + ' '
    nm = nmap.PortScanner()
    scan_result = nm.scan(hosts=lista, arguments='-sP -n -v')

    error_message = "UWAGA!!! awarii uległy następujace urządzenia: "
    error_count = 0
    for ip in scan_result['scan']:
        if 'down' in scan_result['scan'][ip]['status']['state']:
            c.execute("SELECT ping FROM monitoring_device WHERE ip=?", (ip,))
            down_counter = int(c.fetchone()[0])
            print(ip)
            print(down_counter)
            if down_counter == 0:
                c.execute("UPDATE monitoring_device SET status=?, ping=? WHERE ip=?", ('down',1, ip))
                print(ip)
            if int(down_counter) == 1:
                c.execute("UPDATE monitoring_device SET ping=? WHERE ip=?", (2, ip))
                print(ip + 'afdasf')
            if int(down_counter) == 2:
                c.execute("UPDATE monitoring_device SET ping=?, last_seen=? WHERE ip=?", (3, datetime.datetime.now().strftime("%y-%m-%d %H:%M"), ip))
                error_message += ", " + ip
                error_count += 1
            if error_count != 0:
                error_email(error_message)
        else:
            c.execute("UPDATE monitoring_device SET status=?, ping=?, last_seen=? WHERE ip=?", ('up', 0, '-', ip))
    data_base.commit()
    data_base.close()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../../')
    ping()