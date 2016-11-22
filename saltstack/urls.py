from django.conf.urls import patterns, include, url
from saltstack import views

urlpatterns = [
     url(r'^salt-api$', views.index,name='salt-api'),
               ]