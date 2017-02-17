import models
from salt import settings

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