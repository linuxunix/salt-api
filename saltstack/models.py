#_*_coding:utf-8_*_
from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User

class Project_deploy_create(models.Model):
    project_name = models.CharField(max_length=254,verbose_name=u'项目名字',unique=True)
    project_env_choices=(
        (u'dev_env',u'灰度发布'),
        (u'pro_env',u'正式坏境'),
    )
    code_env_choices=(
        (u'git',u'git'),
        (u'svn',u'svn'),
    )
    project_language_choices=(
        (u'php',u'php'),
        (u'java',u'java'),
    )
    project_env = models.CharField(choices=project_env_choices, max_length=128,verbose_name=u'项目坏境')
    project_addr = models.CharField(max_length=254,verbose_name=u'项目地址')
    code_env = models.CharField(choices=code_env_choices, max_length=128,verbose_name=u'代码坏境')
    project_language = models.CharField(choices=project_language_choices, max_length=128,verbose_name=u'项目语言')
    deploy_dir = models.CharField(max_length=254,verbose_name=u'发布主机存放代码目录')
    target_webroot =  models.CharField(max_length=254,verbose_name=u'目标主机Webroot家目录')
    target_releases = models.CharField(max_length=254,verbose_name=u'目标主机版本库目录')
    target_server = models.CharField(max_length=254,verbose_name=u'目标主机地址')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    def __unicode__(self):
        return self.project_name

class Project_deploy_status(models.Model):
    deploy_user = models.CharField(max_length=254,verbose_name=u'开发者')
    project_name = models.CharField(max_length=254,verbose_name=u'项目名字')
    project_commit =  models.CharField(max_length=254,verbose_name=u'项目备注')
    code_branch = models.CharField(max_length=254,verbose_name=u'代码分支')
    code_version = models.CharField(max_length=254,verbose_name=u'版本号')
    salt_jid = models.CharField(max_length=254)
    start_time = models.DateTimeField(verbose_name=u'开始时间')
    finish_time = models.DateTimeField(verbose_name=u'开始时间',null=True)
    status_choices= (('success','Success'),('failed','Failed'),('unknown','Unknown'))
    status = models.CharField(choices=status_choices,max_length=30,default='unknown')
    def __unicode__(self):
        return self.project_name
