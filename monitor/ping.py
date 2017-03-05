import sqlite3
import nmap

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
        c.execute("UPDATE monitoring_device SET status=? WHERE ip=?", ('down', ip))
    else:
        c.execute("UPDATE monitoring_device SET status=? WHERE ip=?", ('up', ip))


data_base.commit()
data_base.close()