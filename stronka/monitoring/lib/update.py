import subprocess
import sqlite3


def update(ip_to_update):
    data_base = sqlite3.connect('db.sqlite3')
    c = data_base.cursor()
    host_configurations = {}

    for ip in ip_to_update:
        c.execute("SELECT ip, login, password, port, firmware FROM monitoring_device WHERE ip=?", (ip,))
        config = c.fetchone()
        host_configurations[config[0]] = {'user': config[1], 'password': config[2], 'port': config[3], 'firmware': config[4]}

    data_base.commit()
    print(host_configurations)
    #client = ParallelSSHClient(hosts=host_configurations.keys(), host_config=host_configurations, num_retries=1)
    #output = client.run_command('mca-status', stop_on_errors=False)

#command = "sshpass -p %s scp -P %s -o ConnectTimeout=5 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -oKexAlgorithms=+diffie-hellman-group1-sha1 /home/karol/programy/monitoring/stronka/monitoring/lib/soft/xm.bin %s@%s:/tmp/xm.bin" %(password, port, user, ip_add)
##command = "curl --anyauth -k scp://%s:%s@%s:%s/tmp/system.cfg -o ~/%s" %(user, password, ip_add, port, ip_add)
#p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
#(output, err) = p.communicate()
#p.kill    
