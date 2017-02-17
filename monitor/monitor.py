from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, \
  UnknownHostException, ConnectionErrorException
import sqlite3

def ParallelSSH(ip_table, other_config, command):

    data_base = sqlite3.connect('../stronka/db.sqlite3')
    c = data_base.cursor()
    c.execute('SELECT ip FROM monitoring_device')
    ip_list = c.fetchall()
    lista = []
    for i in ip_list:
        lista.append(i[0])

    client = ParallelSSHClient(lista, user='', password='', port=22, num_retries=1)
    output = client.run_command('mca-status', stop_on_errors=False)
    for node in output:
        device = {'dev_name':'', 'firmware':'', 'wireless_mode':'', 'signal':0, 'ccq':0, 'air_q':0, 'air_c':0, 'freq':0, 'uptime':0, 'product':'', 'exception':''}
           
        if str(output[node]['exception']) == 'None':
            device['exception'] = 'OK'
            for line in output[node]['stdout']:
                if 'wlanOpmode' in line:
                    device['wireless_mode'] = line.split('=')[1]
                if 'signal' in line:
                    device['signal'] = int(line.split('-')[1])
                if 'ccq' in line:
                    device['ccq'] = int(float(line.split('=')[1])/10)
                if 'uptime' in line:
                    device['uptime'] = int(line.split('=')[1])/86400

                if 'deviceName' in line:
                    line2 = line.split(',')
                    for i in line2:
                        if 'Name' in i:
                            device['dev_name'] = i.split('=')[1]
                        if 'firmware' in i:
                            device['firmware'] = i.split('=')[1]
                        if 'platform' in i:
                            device['product'] = i.split('=')[1]
            c.execute("UPDATE monitoring_device SET dev_name=?, firmware=?, product=?, wireless_mode=?, signal=?, ccq=?, uptime=?, error=? WHERE ip=?", (device['dev_name'], device['firmware'], device['product'], device['wireless_mode'], device['signal'], device['ccq'], device['uptime'], device['exception'], node))     
            
        else:
            device['exception'] = 'failure'
            c.execute("UPDATE monitoring_device SET error=? WHERE ip=?", (device['exception'], node))     
    data_base.commit()
ParallelSSH('dfd', 4, 7)