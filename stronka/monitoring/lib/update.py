import subprocess
import sqlite3



ip_add = '192.168.6.50'
user = 'root'
password = "\"" + 'Kotka09' + "\""
port = "9922"
command = "sshpass -p %s scp -P %s -o ConnectTimeout=10 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -oKexAlgorithms=+diffie-hellman-group1-sha1 /home/karol/programy/monitoring/stronka/monitoring/lib/soft/xm.bin %s@%s:/tmp/xm.bin" %(password, port, user, ip_add)
#command = "curl --anyauth -k scp://%s:%s@%s:%s/tmp/system.cfg -o ~/%s" %(user, password, ip_add, port, ip_add)
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p.kill
    