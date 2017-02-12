import nmap

nm = nmap.PortScanner()

result = nm.scan(hosts='192.168.100.115, 192.168.100.116', ports='10001', arguments='-sU')
print(result)