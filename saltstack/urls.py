from django.conf.urls import patterns, include, url
from saltstack import views

urlpatterns = [
         url(r'^salt-api/$', views.salt_api,name='salt-api'),
         url(r'^accepted_key/$', views.accepted_key, name='accepted_key'),
         url(r'^delete_key/$', views.delete_key, name='delete_key'),
         url(r'^salt_test/$', views.salt_test, name='salt_test'),
    ]