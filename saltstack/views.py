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

