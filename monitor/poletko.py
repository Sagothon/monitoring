import nmap

nm = nmap.PortScanner()
scan_result = nm.scan(arguments='-v -sn -iL ./list')
print(scan_result)