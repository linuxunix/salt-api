import models
from salt import settings
from django.shortcuts import get_object_or_404
import os,datetime,time


class Project_deploy_create(object):
    def __init__(self,request):
        self.request = request
    def parse_data(self):
        form_data = {
        'project_name' : self.request.POST.get('project_name'),
        'project_env':  self.request.POST.get('project_env'),
        'project_addr' :  self.request.POST.get('project_addr'),
        'code_env':  self.request.POST.get('code_env'),
        'project_language': self.request.POST.get('project_language'),
        'deploy_dir':self.request.POST.get('deploy_dir'),
        'target_webroot':self.request.POST.get('target_webroot'),
        'target_releases':self.request.POST.get('target_releases'),
        'target_server':self.request.POST.get('target_server'),
        }
        return form_data
    def create(self):
        self.data = self.parse_data()
        project_obj = models.Project_deploy_create(**self.data)
        project_obj.save()
    def edit(self):
        self.data = self.parse_data()
        models.Project_deploy_create.objects.get(project_name=self.request.POST.get('project_name')).delete()
        project_obj = models.Project_deploy_create(**self.data)
        project_obj.save()
class Project_deploy_status(object):
    def __init__(self,request):
        self.request = request
    def deploy(self):
        project = get_object_or_404(models.Project_deploy_create, pk=self.request.GET.get('id'))
        deploy_status = models.Project_deploy_status(deploy_user=self.request.user,
                                                     code_branch=self.request.POST.get('code_branch'),
                                                     project_name=project.project_name,
                                                     project_commit=self.request.POST.get('project_commit'),
                                                     code_version=self.request.POST.get('code_version'),
                                                     start_time=datetime.datetime.now())
        deploy_status.save()
        os.system('touch /var/run/deploy.lock')
        dir = project.deploy_dir + "/code/" + project.project_name
        tmp_dir = project.deploy_dir + "/tmp/"
        dir_tar = project.project_name+'_'+self.request.POST.get('code_branch').split('/')[1]+'_'+self.request.POST.get('code_version')+'_'+ time.strftime("%Y-%m-%d_%H_%M_%S",time.gmtime())+'.tar.gz'
        cmd = "tar czf {0} {1} && mv dir_tar {2}".format(dir_tar,dir,tmp_dir)
        # os.system(cmd)
        print cmd
        
        os.system('rm -r /var/run/deploy.lock ')
