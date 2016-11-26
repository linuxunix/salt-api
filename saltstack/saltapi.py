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
        form = {'client': 'wheel', 'fun': 'key.list_all'}
        form_data = urllib.urlencode(form)
        headers = {'X-Auth-Token': self.salt_login_token()}
        request = urllib2.Request(
            url=self._url,
             headers=headers,
            data=form_data
        )
        response = json.load(urllib2.urlopen(request))
        #Accepted Keys:
        minions = response['return'][0]['data']['return']['minions']
        #Unaccepted Keys:
        minions_pre = response['return'][0]['data']['return']['minions_pre']
        return minions,minions_pre

    def accept_key(self,node_name):
        form = {'client': 'wheel', 'fun': 'key.accept', 'match': node_name}
        form_data = urllib.urlencode(form)
        headers = {'X-Auth-Token': self.salt_login_token()}
        request = urllib2.Request(
            url=self._url,
             headers=headers,
            data=form_data
        )
        response = json.load(urllib2.urlopen(request))
        if(response['return'][0]['data']['return'] == {}):
            info="添加%s失败，请检查node_name是否正确！"%node_name
        elif(response['return'][0]['data']['return'],response['return'][0]['data']['success'] == 'true'):
            info='添加%s成功！'%node_name
        return info

    def delete_key(self, node_name):
        form = {'client': 'wheel', 'fun': 'key.delete', 'match': node_name}
        form_data = urllib.urlencode(form)
        headers = {'X-Auth-Token': self.salt_login_token()}
        request = urllib2.Request(
            url=self._url,
            headers=headers,
            data=form_data
        )
        response = json.load(urllib2.urlopen(request))
        info = '删除%s成功！' % node_name
        return info

    def salt_remote_execution(self,tgt, fun,arg=0,client='local'):
        if arg == 0:
           form = {'client': client, 'tgt': tgt, 'fun': fun}
        else:
           form = {'client': client, 'tgt': tgt, 'fun': fun, 'arg': arg}

        form_data = urllib.urlencode(form)
        headers = {'X-Auth-Token': self.salt_login_token()}
        request = urllib2.Request(
            url=self._url,
             headers=headers,
            data=form_data
        )
        response = urllib2.urlopen(request)
        return json.load(response)['return'][0]

# print SaltAPI().salt_remote_execution(tgt='*',fun='test.ping')
# print SaltAPI().salt_remote_execution(tgt='*',fun='cmd.run',arg='ifconfig')
# print SaltAPI().list_all_key()
# print SaltAPI().accept_key(node_name='192.168.1.237')
# print SaltAPI().delete_key('192.168.1.248')
