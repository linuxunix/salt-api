# -*- coding: utf-8 -*-
from django.shortcuts import render
from saltapi import SaltAPI
from mysqlapi import MysqlApi
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "salt.settings")
try:
    import json
except ImportError:
    import simplejson as json

from saltstack.applet.decorators import page_render

def salt_api(request):
    Accepted_Keys = SaltAPI().list_all_key()[0]
    Unaccepted_Keys=SaltAPI().list_all_key()[1]
    return render(request, 'SaltStack/salt-api.html', locals())

@csrf_exempt
def accepted_key(request):
    node_name = request.POST.get('Unaccepted_Key[]')
    result=SaltAPI().accept_key(node_name=str(node_name))
    return HttpResponse(json.dumps(result))

@csrf_exempt
def delete_key(request):
    node_name = request.POST.get('Accepted_Key[]')
    result=SaltAPI().delete_key(node_name=str(node_name))
    return HttpResponse(json.dumps(result))

@csrf_exempt
def salt_test(request):
    result=[]
    result_show = []
    node_name = request.POST.getlist('Select_Host[]')
    if len(node_name) > 1:
        for i in node_name:
            result.append(SaltAPI().salt_remote_execution(tgt=str(i), fun='test.ping'))

        return HttpResponse(json.dumps(str(result)),content_type='application/json')

    else:
        result.append(SaltAPI().salt_remote_execution(tgt=str(node_name[0]),fun='test.ping'))
        return HttpResponse(json.dumps(str(result[0][0])),content_type='application/json')


@csrf_exempt
def salt_many_cmd(request):
    Accepted_Keys = SaltAPI().list_all_key()[0]
    result=[]
    if request.method=='POST':
        cmd_args = request.POST.get('cmd_args')
        match = request.POST.getlist('match[]')
        for i in  match:
            result.append(SaltAPI().salt_remote_execution(client='local_async',tgt=str(i),fun='cmd.run',arg=cmd_args))
        return HttpResponse(json.dumps(result))
    return render(request, 'SaltStack/salt_many_cmd.html',{'Accepted_Keys':Accepted_Keys})

def salt_cmd_result(request):
    jids = request.GET.getlist('jids[]')
    result=[]
    for i in jids:
        result.append(MysqlApi().salt_returns(i))
    return HttpResponse(json.dumps(result))

@csrf_exempt
def salt_deploy(request):
    print request.POST
    cmd = {'aliyum': 'aliyum.aliyum','jdk':'Jdk_Tomcat.jdk_install','tomcat1.8':'Jdk_Tomcat.tomcat8_install','nginx':'nginx.nginx_install','nginx.conf':'nginx.nginx_conf'}
    fun = 'state.sls'
    result = []
    error =""
    Accepted_Keys = SaltAPI().list_all_key()[0]
    if request.method == 'POST':
        select_app = request.POST.get('select_app')
        match = request.POST.getlist('match[]')
        ssh_id= request.POST.get('ssh_id')
        if select_app=='' and ssh_id != '':
            ssh_id = request.POST.get('ssh_id').split(',')
        ##判断match和ssh_id都为''
        # if match ==''and ssh_id=='':
        error = '请选择执行主机或者输入salt_id'
        for i in match:
            result.append(SaltAPI().salt_remote_execution(client='local_async',tgt=str(i),fun=fun,arg=cmd[select_app]))
        return HttpResponse(json.dumps(result))
    return render(request, 'SaltStack/salt_deploy.html', {'Accepted_Keys':Accepted_Keys})


salt_dir='SaltStack/'
@page_render( salt_dir+"salt-api.html")
def test2(request):
    pass


def salt_web_deploy(request):
    Accepted_Keys = SaltAPI().list_all_key()[0]
    return render(request, 'SaltStack/salt_web_deploy.html', locals())





















