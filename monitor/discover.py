import nmap
import sqlite3

data_base = sqlite3.connect('../stronka/db.sqlite3')
c = data_base.cursor()

def ubnt_discovery(networks_to_scan):
    
    nm = nmap.PortScanner()
    networks_to_scan = '192.168.100.0/24'
    scan_result = nm.scan(hosts=networks_to_scan, ports='10001', arguments='-sU')
    file = open('ubnt_list', 'w')
    ubnt_scan_result = []

    for key in scan_result['scan']:
        if 'open' in scan_result['scan'][key]['udp'][10001]['state']:
            
            c.execute('insert into monitoring_device(ip) values(?)', (str(key),))
            data_base.commit()
            file.write('%s\n' % str(key))

#TO DO:
#   for loop to scan networks passed to function
 
ubnt_discovery('dsfds')