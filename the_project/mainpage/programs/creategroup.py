from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import CreateGroupForm

class CreateGroup(TemplateView):
    def __init__(self):
        self.params = {
            "form" : CreateGroupForm()["group_name"],
            "group_name" : ""
        }
    def get(self, request, project_id):

        self.params["project_name"] = project_id
        return render(request, 'mainpage/creategroup.html', self.params)

    def post(self, request, project_id):
        self.params["project_name"] = project_id
        group_name = request.POST.get("group_name")
        project_id = project_id


        recordable = True

        if recordable:
            group = Group(
                project_id = Project.objects.get(uuid=project_id),
                group_name=group_name,
            )
            group.save()
            self.params["message"] = group_name + "を作成しました"
            
            return render(request, 'mainpage/creategroup.html', self.params)
