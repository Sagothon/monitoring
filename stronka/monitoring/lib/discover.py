import sqlite3
import subprocess
import re

def ubnt_discovery(data_from_form):

    data_base = sqlite3.connect('db.sqlite3')
    c = data_base.cursor()

    network_to_scan = data_from_form['ip']
    print(network_to_scan)
    login = data_from_form['login']
    password = data_from_form['password']
    port = data_from_form['port']

    cmd = "sudo nmap -n -sU --open %s -p 10001 -oG scan" % network_to_scan
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = p.communicate()
    p.kill

    file = open('scan', 'r')

    for line in file:
        if 'open' in line:
            result = re.search(': (.*) \(', line)
            if result is not None:
                c.execute('insert into monitoring_device(ip, login, password, port, ping) values(?, ?, ?, ?, ?)', (result.group(0)[2:-2], login, password, int(port), 0))

    data_base.commit()
