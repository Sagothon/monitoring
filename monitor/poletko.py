from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, \
  UnknownHostException, ConnectionErrorException

host_config = { 'host1' : {'user': 'user1', 'password': 'pass',
                           'port': 2222},
                'host2' : {'user': 'user2', 'password': 'pass',
                           'port': 2223},
                }
for key in host_config:
    print(key)
    print(host_config[key]['password'])

dictionary = {'user': 'user5', 'password': 'haselko', 'port': 9922}
host_config['23443'] = dictionary
print(host_config)
#client = ParallelSSHClient(lista, user='', password='', port=22, num_retries=1)
#output = client.run_command('mca-status', stop_on_errors=False)