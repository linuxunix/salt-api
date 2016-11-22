from django.shortcuts import render
from saltapi import *
# Create your views here.

def index(request):
    minions_list = SaltAPI().list_all_key()

    return render(request, 'SaltStack/salt-api.html', locals())

