from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, \
  UnknownHostException, ConnectionErrorException
import subprocess
import sqlite3

def update(hosts_list):
    data_base = sqlite3.connect('../../db.sqlite3')
    c = data_base.cursor()
    c.execute('SELECT ip, login, password, port, firmware FROM monitoring_device')

    config = c.fetchall()
    host_configurations = {}
    for ip in config:
        if ip[0] in hosts_list:
            host_configurations[ip[0]] = {'user': ip[1], 'password': ip[2], 'port': ip[3], 'firmware': ip[4]}
    print(host_configurations)
    command = "sshpass -p %s scp -P %s -o ConnectTimeout=10 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -oKexAlgorithms=+diffie-hellman-group1-sha1 %s@%s:/tmp/system.cfg /home/karol/programy/monitoring/backup/%s" %(password, port, user, ip_add, ip_add)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p.kill

update('192.168.100.62')
