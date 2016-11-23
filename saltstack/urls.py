from django.conf.urls import patterns, include, url
from saltstack import views

urlpatterns = [
     url(r'^salt-api$', views.salt_api,name='salt-api'),
               ]