from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, \
  UnknownHostException, ConnectionErrorException

def update():
    print('dfgdg')

def ParallelSSH(ip_table, other_config, command):

#dorobić host config dla innych konfiguracji

    client = ParallelSSHClient(['192.168.6.226', '192.168.100.10', '192.168.100.11', '192.168.100.244'], user=usr, password=passwd, port=port)
    try:
        output = client.run_command('mca-status', stop_on_errors=False)
        for node in output:
            print(node)
            for line in output[node]['stdout']:
                print(line)
    except (AuthenticationException, UnknownHostException, ConnectionErrorException):
        print(ConnectionErrorException)

ParallelSSH('hjg')