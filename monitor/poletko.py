from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, \
  UnknownHostException, ConnectionErrorException
import sqlite3

data_base = sqlite3.connect('../stronka/db.sqlite3')
c = data_base.cursor()

c.execute('SELECT ip FROM monitoring_device')
ip_list = c.fetchall()
lista = []
for i in ip_list:
  lista.append(i[0])
print(lista)

client = ParallelSSHClient(lista, user='', password='', port=22, num_retries=1)
try:
  output = client.run_command('mca-status', stop_on_errors=False)
except:
  pass

device = {'dev_name':'', 'firmware':'', 'wireless_mode':'', 'signal':0, 'ccq':0, 'air_q':0, 'air_c':0, 'freq':0, 'uptime':0, 'product':''}

for node in output:
    #print(output[node]['exception'])
    for line in output[node]['stdout']:
      if 'WlanOpmode' in line:
        device['wireless_mode'] = i.split('=')[1]

      if 'deviceName' in line:
        line2 = line.split(',')
        for i in line2:
          if 'Name' in i:
            device['dev_name'] = i.split('=')[1]
          if 'firmware' in i:
            device['firmware'] = i.split('=')[1]
          if 'platform' in i:
            device['product'] = i.split('=')[1]

    c.execute("UPDATE monitoring_device SET dev_name=?, firmware=?, product=?  WHERE ip=?", (device['dev_name'], device['firmware'], device['product'], node))     
    data_base.commit()
        