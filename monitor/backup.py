from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, \
  UnknownHostException, ConnectionErrorException
#import sqlite3

#data_base = sqlite3.connect('../stronka/db.sqlite3')
#c = data_base.cursor()
#c.execute('SELECT ip, login, password, port FROM monitoring_device')
#config = c.fetchall()

#host_configurations = {}
#print("fdfgd")
#for ip in config:
#    host_configurations[ip[0]] = {'user': ip[1], 'password': ip[2], 'port': 9922}

client = ParallelSSHClient(hosts=")
client.copy_file(local_file="~/programy/monitoring/backup/siema", remote_file="/tmp/systemm.cfg")
client.copy_remote_file