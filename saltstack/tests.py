# -*- coding: utf-8 -*-
from django.test import TestCase
a='docker,docker1,docker2'
print a.split(',')



# -*- coding: utf-8 -*-
import sys
import nmap
scan_row = [ ]
input_data = raw_input('Please input host and port: ')
scan_row = input_data.split(" ")
if len( scan_row ) !=2:
    print "Input errors,example\"192.168.1.0/24 80,443,22\""
    sys.exit(0)
hosts = scan_row[0]  #接收用户输入的主机
port = scan_row[1]  #接收用户输入的端口
try:
    nm = nmap.PortScanner() #创建端口扫描对象
except nmap.PortScannerError:
    print ('Nmap not found,',sys.exc_info()[0])
    sys.exit(0)
try:
    nm.scan(hosts=hosts,arguments='-v -sS -p'+port)
except Exception,e:
    print "Scan error:"+str(e)
for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
