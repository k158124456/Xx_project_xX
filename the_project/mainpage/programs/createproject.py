from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import CreateProjectForm

class CreateProject(TemplateView):
    def __init__(self):
        self.params = {
            "form" : CreateProjectForm()["project_name"],
            "project_name" : "",
            "message":""

        }
    def get(self, request):
        return render(request, "mainpage/createptoject.html", self.params)

    def post(self, request):
        project_name = request.POST.get("project_name")
        #self.params["project_name"] = Project.objects.all().id

        recordable = True

        if recordable:
            proj = Project(
                project_name = project_name
            )
            proj.save()
            pm = ProjectMember(
                userlist=User.objects.get(username=request.user),
                projectlist=Project.objects.get(project_name=project_name),
                displayname="プロジェクト作成者",
                role=1, 
            )
            pm.save()
            self.params["message"] = project_name + "を作成しました"

            return render(request, "mainpage/createptoject.html", self.params)
        else:

            return render(request, "mainpage/createptoject.html", self.params)

        