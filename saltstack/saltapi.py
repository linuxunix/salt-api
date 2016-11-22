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
    def __init__(self,_url,_user,_pass):
        self._url = _url
        self._user = _user
        self._pass = _pass

    # 登录salt-api,获取token
    def salt_login_token(self):
        form = {'eauth': 'pam', 'username': self._user, 'password': self._pass}
        form_data = urllib.urlencode(form)
        request = urllib2.Request(self._url, form_data)
        response = urllib2.urlopen(request)
        token=json.load(response)
        token_id=token['return'][0]['token']
        return token_id
print SaltAPI(settings.SALT_API_URL_LOGIN,settings.SALT_API_AUTH_USER,settings.SALT_API_AUTH_PASS).salt_login_token()
