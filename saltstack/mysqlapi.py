# -*- coding: utf-8 -*-
from django.conf import settings
#初始化坏境
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weixin.settings")
import django
django.setup()
import MySQLdb
import json

class MysqlApi(object):
    def __init__(self):
        self._host = settings.MYSQL_HOST
        self._user = settings.MYSQL_USER
        self._pass = settings.MYSQL_PASS
        self._db = settings.MYSQL_DB
    def salt_returns(self,jids):
        try:
            conn = MySQLdb.connect(host=self._host, user=self._user, passwd=self._pass, db=self._db)
            cur = conn.cursor()
            recount = cur.execute("select full_ret from salt_returns where jid='%s'"%jids)
            date = cur.fetchall()
            ###str==>dict
            return json.loads(date[0][0])
            cur.close()
            conn.close()
        except MySQLdb.Error, e:
            print "Mysql Error %d:%s" % (e.args[0], e.args[1])
#
# print MysqlApi().salt_returns('20161202110135156194 ')['return']