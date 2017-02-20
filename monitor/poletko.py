from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, \
  UnknownHostException, ConnectionErrorException
import sqlite3

data_base = sqlite3.connect('../stronka/db.sqlite3')
c = data_base.cursor()
c.execute('SELECT ip, login, password, port FROM monitoring_device')
config = c.fetchall()

host_conf = {}
for ip in config:
    host_conf[ip[0]] = {'user': ip[1], 'password': ip[2], 'port': 9922}

client = ParallelSSHClient(hosts=host_conf.keys(), user='', password='', port=9922, num_retries=1)
print(client.run_command('mca-status', stop_on_errors=False))