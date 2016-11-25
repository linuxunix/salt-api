from django.conf.urls import patterns, include, url
from saltstack import views

urlpatterns = [
         url(r'^salt-api/$', views.salt_api,name='salt-api'),
         url(r'^accepted_key/$', views.accepted_key, name='accepted_key'),
         url(r'^delete_key/$', views.delete_key, name='delete_key'),
         url(r'^salt_test/$', views.salt_test, name='salt_test'),
         url(r'^salt_many_cmd/$', views.salt_many_cmd, name='salt_many_cmd'),
         url(r'^salt_cmd_result/$', views.salt_cmd_result, name='salt_cmd_result'),
    ]