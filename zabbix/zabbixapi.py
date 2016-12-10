# -*- coding: utf-8 -*-
from django.conf import settings
#初始化坏境
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weixin.settings")
import django
django.setup()
import MySQLdb
import json
from zabbix.api import ZabbixAPI


zapi = ZabbixAPI(url='http://10.6.17.83:8080/zabbix/', user='admin', password='zabbix@good')
result1 = zapi.host.get(monitored_hosts=1, output='extend')
item_list = zapi.do_request('item.get',
                          {
                              "output": "extend",
                              "host": "Zabbix server",
                              "search": {
                                  "key_": "system"
                              },
                          })
print len( [host["host"] for host in result1])
print item_list["result"]


