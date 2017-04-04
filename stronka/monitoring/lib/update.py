from pssh import ParallelSSHClient, utils
from gevent import joinall

utils.enable_logger(utils.logger)
hosts = ['']
client = ParallelSSHClient(hosts, )
greenlets = client.copy_file('../test', 'test_dir/test')
joinall(greenlets, raise_error=True)
