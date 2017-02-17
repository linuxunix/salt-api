from django.conf.urls import include, url
from saltstack import views
from saltstack.applet.decorators import page_render


urlpatterns = [
         url(r'^salt-api/$', views.salt_api,name='salt-api'),
         url(r'^accepted_key/$', views.accepted_key, name='accepted_key'),
         url(r'^delete_key/$', views.delete_key, name='delete_key'),
         url(r'^salt_test/$', views.salt_test, name='salt_test'),
         url(r'^salt_many_cmd/$', views.salt_many_cmd, name='salt_many_cmd'),
         url(r'^salt_cmd_result/$', views.salt_cmd_result, name='salt_cmd_result'),
         url(r'^salt_deploy/$', views.salt_deploy, name='salt_deploy'),
         url(r'^salt_web_deploy/$', views.salt_web_deploy, name='salt_web_deploy'),
         url(r'^salt_project_new/$', views.salt_project_new, name='salt_project_new'),
         url(r'^project_web_deploy/$', views.project_web_deploy, name='project_web_deploy'),
         url(r'^project_web_deploy_edit/$', views.project_web_deploy_edit, name='project_web_deploy_edit'),
    ]