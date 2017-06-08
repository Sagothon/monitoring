from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, \
  UnknownHostException, ConnectionErrorException
import sqlite3
import os
from datetime import datetime, timedelta
import time

def monitor():
    
    data_base = sqlite3.connect('db.sqlite3')
    c = data_base.cursor()
    c.execute('SELECT ip, login, password, port FROM monitoring_device')
    config = c.fetchall()
    host_configurations = {}
    for ip in config:
        host_configurations[ip[0]] = {'user': ip[1], 'password': ip[2], 'port': ip[3]}
    client = ParallelSSHClient(hosts=host_configurations.keys(), host_config=host_configurations, num_retries=1)
    output = client.run_command('mca-status', stop_on_errors=False)
    for node in output:
        device = {'dev_name':'', 'firmware':'', 'wireless_mode':'', 'signal':0, 'ccq':0, 'air_q':0, 'air_c':0, 'freq':0, 'uptime':'', 'product':'', 'exception':''}
        if str(output[node]['exception']) == 'None':
            device['exception'] = 'OK'
            for line in output[node]['stdout']:
                if 'wlanOpmode' in line:
                    if 'sta' in str(line.split('=')[1]):
                        device['wireless_mode'] = 'station'
                    if 'ap' in str(line.split('=')[1]):
                        device['wireless_mode'] = 'access point'
                if 'signal' in line:
                    device['signal'] = int(line.split('-')[1])
                if 'ccq' in line:
                    device['ccq'] = int(float(line.split('=')[1])/10)
                if 'uptime' in line:
                    seconds = int(line.split('=')[1])
                    print(seconds)
                    days, seconds = divmod(seconds, 24*60*60)
                    hours, seconds = divmod(seconds, 60*60)
                    minutes, seconds = divmod(seconds, 60)
                    time = '%s d %s h %s m' % (days,hours,minutes)
                    device['uptime'] = str(time)
                if 'deviceName' in line:
                    line2 = line.split(',')
                    for i in line2:
                        if 'Name' in i:
                            if '==' in i:
                                device['dev_name'] = i.split('=')[1] + '==' + i.split('==')[1]
                            else:
                                device['dev_name'] = i.split('=')[1]
                        if 'firmware' in i:
                            device['firmware'] = i.split('=')[1][0:16]
                        if 'platform' in i:
                            device['product'] = i.split('=')[1]
            c.execute("UPDATE monitoring_device SET dev_name=?, firmware=?, product=?, wireless_mode=?, signal=?, ccq=?, uptime=?, error=? WHERE ip=?", (device['dev_name'], device['firmware'], device['product'], device['wireless_mode'], device['signal'], device['ccq'], device['uptime'], device['exception'], node))
        else:
            device['exception'] = 'login failure'
            c.execute("UPDATE monitoring_device SET error=? WHERE ip=?", (device['exception'], node))     
    data_base.commit()
    data_base.close()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../../')
    monitor()