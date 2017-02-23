from django.contrib import admin

# Register your models here.

from saltstack import models
admin.site.register(models.Project_deploy_create)
admin.site.register(models.Project_deploy_status)
