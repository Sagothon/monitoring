import nmap
import sqlite3

def ubnt_discovery(networks_to_scan):

    data_base = sqlite3.connect('../stronka/db.sqlite3')
    c = data_base.cursor()

    nm = nmap.PortScanner()
    scan_result = nm.scan(hosts=networks_to_scan, ports='10001', arguments='-sU')
    file = open('ubnt_list', 'w')

    for ip_address in scan_result['scan']:
        if 'open' in scan_result['scan'][ip_address]['udp'][10001]['state']:

            c.execute('insert into monitoring_device(ip, login, password, port) values(?, ?, ?, ?)', (str(ip_address), 'root', 'Kotka09', 9922))
            data_base.commit()
            file.write('%s\n' % str(ip_address))

networks = '192.168.100.0/24'
ubnt_discovery(networks)
