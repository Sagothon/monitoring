import sqlite3
import nmap
import datetime
import smtplib
from email.mime.text import MIMEText

def error_email(message):
    # Create a text/plain message
    msg = MIMEText('siema', 'plain')
    
    me = 'siema@wer.pl'
    you = ''
    msg['Subject'] = 'The contents of'
    msg['From'] = me
    msg['To'] = you
    
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail(me, [you], msg.as_string())
    s.quit()

data_base = sqlite3.connect('../stronka/db.sqlite3')
c = data_base.cursor()
c.execute('SELECT ip FROM monitoring_device')
ip_list = c.fetchall()
lista=''
file = open('ip_list', 'w+')
for i in ip_list:
    file.write(i[0] + '\n')
    lista += i[0] + ' '

nm = nmap.PortScanner()
scan_result = nm.scan(hosts=lista, arguments='-sP -n -v')

for ip in scan_result['scan']:
    if 'down' in scan_result['scan'][ip]['status']['state']:
        print(ip)
        c.execute("SELECT ping FROM monitoring_device WHERE ip=?", (ip,))
        down_counter = c.fetchone()[0]
        print(down_counter)
        if down_counter == 'None':
            c.execute("UPDATE monitoring_device SET status=?, ping=? WHERE ip=?", ('down',1, ip))
        if int(down_counter) == 1:
            c.execute("UPDATE monitoring_device SET ping=? WHERE ip=?", (2, ip))
        if int(down_counter) == 2:
            c.execute("UPDATE monitoring_device SET last_seen=? WHERE ip=?", (datetime.datetime.now().strftime("%y-%m-%d %H:%M"), ip))
            error_email(2)
    else:
        c.execute("UPDATE monitoring_device SET status=?, ping=? WHERE ip=?", ('up',0, ip))

data_base.commit()
data_base.close()