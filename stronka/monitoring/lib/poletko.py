import os
import subprocess
import sqlite3
import datetime
import sys
from subprocess import check_output

data_base = sqlite3.connect('../../db.sqlite3')
c = data_base.cursor()
c.execute('SELECT ip, id FROM monitoring_device')
ip_list = c.fetchall()

for i in ip_list:
    print(i)
    dev_id = i[1] 
    host = i[0]

    out = check_output(['ping', '-c', '3', host]).decode(sys.stdout.encoding)

    avg_ping = out[-21:-16]
    c.execute("INSERT INTO monitoring_ping_history (avg, date, device_id) VALUES (?,?,?)", (avg_ping,datetime.datetime.now().strftime("%y-%m-%d %H:%M"),dev_id))
    
data_base.commit()
data_base.close()