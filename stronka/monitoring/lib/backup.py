import subprocess
import sqlite3
import os

def back_it_up():
    data_base = sqlite3.connect('db.sqlite3')
    c = data_base.cursor()
    c.execute('SELECT ip, login, password, port FROM monitoring_device')
    config = c.fetchall()
    data_base.close()

    for ip in config:
        ip_add = ip[0]
        user = ip[1]
        password = "\"" + ip[2] + "\""
        port = "9922"

        command = "sshpass -p %s scp -P %s -o ConnectTimeout=10 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -oKexAlgorithms=+diffie-hellman-group1-sha1 %s@%s:/tmp/system.cfg /home/karol/programy/monitoring/backup/%s" %(password, port, user, ip_add, ip_add)
        #command = "curl --anyauth -k scp://%s:%s@%s:%s/tmp/system.cfg -o ~/%s" %(user, password, ip_add, port, ip_add)

        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.kill

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__) + '/../../')
