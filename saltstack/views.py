from django.shortcuts import render
from saltapi import *
# Create your views here.

def salt_api(request):
    Accepted_Keys = SaltAPI().list_all_key()[0]
    Unaccepted_Keys=SaltAPI().list_all_key()[1]
    return render(request, 'SaltStack/salt-api.html', locals())

def accepted_keys(request,match):
    if request.method == 'POST':
        node_name=request.method.get('match')
        print  node_name