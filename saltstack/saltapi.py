# -*- coding: utf-8 -*-
from django.conf import settings
import urllib2,urllib
import json
#初始化坏境
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weixin.settings")
import django
django.setup()

class SaltAPI(object):
    _token_id = ''
    def __init__(self):
        self._login_url = settings.SALT_API_URL_LOGIN
        self._url = settings.MASTER_API_URL
        self._user = settings.SALT_API_AUTH_USER
        self._pass = settings.SALT_API_AUTH_PASS

    # 登录salt-api,获取token
    def salt_login_token(self):
        form = {'eauth': 'pam', 'username': self._user, 'password': self._pass}
        form_data = urllib.urlencode(form)
        request = urllib2.Request(self._login_url, form_data)
        response = urllib2.urlopen(request)
        token=json.load(response)
        token_id=token['return'][0]['token']
        return token_id

    def list_all_key(self):
        form = {'client': 'whell', 'fun': 'key.list_all'}
        form_data = urllib.urlencode(form)
        headers = {'X-Auth-Token': SaltAPI().salt_login_token()}
        request = urllib2.Request(
            url=self._url,
             headers=headers,
            data=form_data
        )
        response = urllib2.urlopen(request)
        return  json.load(response)
    def salt_remote_noarg_execution(self, tgt, fun):
        form = {'client': 'local', 'tgt': tgt, 'fun': fun}
        form_data = urllib.urlencode(form)
        headers = {'X-Auth-Token': SaltAPI().salt_login_token()}
        request = urllib2.Request(
            url=self._url,
             headers=headers,
            data=form_data
        )
        response = urllib2.urlopen(request)
        return  json.load(response)

    def salt_remote_execution(self, tgt, fun,arg):
        form = {'client': 'local', 'tgt': tgt, 'fun': fun,'arg':arg}
        form_data = urllib.urlencode(form)
        headers = {'X-Auth-Token': SaltAPI().salt_login_token()}
        request = urllib2.Request(
            url=self._url,
             headers=headers,
            data=form_data
        )
        response = urllib2.urlopen(request)
        return  json.load(response)


#测试
print SaltAPI().salt_remote_noarg_execution(tgt='*',fun='disk.usage')
#print  SaltAPI().salt_remote_execution(tgt='*',fun='cmd.run',arg='free -m')

