import subprocess
import sqlite3

data_base = sqlite3.connect('../stronka/db.sqlite3')
c = data_base.cursor()
c.execute('SELECT ip, login, password, port FROM monitoring_device')
config = c.fetchall()

host_configurations = {}
print(config)

for ip in config:
    host_configurations[ip[0]] = {'user': ip[1], 'password': ip[2], 'port': 9922}
    ip_add = ip[0]
    user = ip[1]
    password = "\"" + ip[2] + "\""
    port = "9922"

    command = "sshpass -p %s scp -P %s -o StrictHostKeyChecking=no root@%s:/tmp/system.cfg /home/karol/programy/monitoring/back/%s" %(password, port, ip_add, ip_add)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()


#command = "sshpass -p \"Kotka09\" scp -P 9922 root@192.168.5.100:/tmp/system.cfg /home/karol/programy/monitoring/back/conf"

#