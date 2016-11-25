# -*- coding: utf-8 -*-
from django.shortcuts import render
from saltapi import SaltAPI
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
        print request.POST
        cmd_args = request.POST.get('cmd_args')
        match = request.POST.getlist('match[]')
        for i in  match:
            result.append(SaltAPI().salt_remote_execution(client='local_async',tgt=str(i),fun='cmd.run',arg=cmd_args))
        print result
        return HttpResponse(json.dumps(result))
    return render(request, 'SaltStack/salt_many_cmd.html',{'Accepted_Keys':Accepted_Keys})