from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import NewDisplayName, NewProjectName
from django.urls import reverse
from urllib.parse import urlencode
from copy import copy

class ProjectSettings(TemplateView):
    def __init__(self):
        self.params = {

        }
    def get(self, request, project_id):
        self.params = {
            "project_uuid" : project_id,
        }
        role = ProjectMember.objects.filter(projectlist__uuid=project_id).get(userlist=request.user).role
        self.params["role"] = role
        return render(request, 'mainpage/project_settings_main.html', self.params)

class ProjectSettings_nemesetting(TemplateView):
    def __init__(self):
        self.params = {

        }
    def get(self, request, project_id):
        self.params = {
            "project_uuid" : project_id,
            "form" : NewProjectName()["new_project_name"],
            "message" : ""
        }
        role = ProjectMember.objects.filter(projectlist__uuid=project_id).get(userlist=request.user).role
        self.params["role"] = role
        return render(request, 'mainpage/project_settings_namesetting.html', self.params)
    def post(self, request, project_id):
        self.params = {
            "project_uuid" : project_id,
            "form" : NewProjectName()["new_project_name"],
            "message" : ""
        }
        role = ProjectMember.objects.filter(projectlist__uuid=project_id).get(userlist=request.user).role
        self.params["role"] = role
        project = Project.objects.get(uuid=project_id)
        new_project_name = request.POST.get("new_project_name")
        project.project_name = new_project_name
        project.save()
        self.params["message"] = "新しいプロジェクト名を”" + new_project_name + "”に設定しました"
        return render(request, 'mainpage/project_settings_namesetting.html', self.params)

class ProjectSettings_display_name(TemplateView):
    def __init__(self):
        self.params = {

        }
    def get(self, request, project_id):
        self.params = {
            "project_uuid" : project_id,
            "form" : NewDisplayName()["new_display_name"],
            "message" : ""
        }
        role = ProjectMember.objects.filter(projectlist__uuid=project_id).get(userlist=request.user).role
        self.params["role"] = role
        return render(request, 'mainpage/project_settings_display_name.html', self.params)
    
    def post(self, request, project_id):
        self.params = {
            "project_uuid" : project_id,
            "form" : NewDisplayName()["new_display_name"],
            "message" : ""
        }
        role = ProjectMember.objects.filter(projectlist__uuid=project_id).get(userlist=request.user).role
        self.params["role"] = role
        project = ProjectMember.objects.filter(projectlist__uuid=project_id)
        user = project.get(userlist=request.user)
        new_display_name = request.POST.get("new_display_name")
        user.displayname = new_display_name
        user.save()
        self.params["message"] = "新しい表示名を”" + new_display_name + "”に設定しました"
        return render(request, 'mainpage/project_settings_display_name.html', self.params)

class ProjectSettings_member(TemplateView):
    def __init__(self):
        self.params = {

        }
    def get(self, request, project_id):
        self.params = {
            "project_uuid" : project_id
        }
        role = ProjectMember.objects.filter(projectlist__uuid=project_id).get(userlist=request.user).role
        self.params["role"] = role
        all_members = ProjectMember.objects.filter(projectlist__uuid=project_id)
        members = all_members.exclude(userlist=request.user)
        own = all_members.get(userlist=request.user)
        self.params["me"] = own
        self.params["userlist"] = members
        return render(request, 'mainpage/project_settings_member.html', self.params)

class ProjectSettings_member_change(TemplateView):
    def __init__(self):
        self.params = {

        }
    def get(self, request, project_id):
        the_user = request.GET["username"]
        pm = ProjectMember.objects.filter(projectlist__uuid=project_id).get(userlist__username=the_user)
        role = copy(pm.role)
        if role == 1:
            pm.role = 0
        if role == 0:
            pm.role = 1
        pm.save()
            
        return redirect("/mainpage/project_"+project_id+"/setting/member")

class ProjectSettings_delete(TemplateView):
    def __init__(self):
        self.params = {

        }
    def get(self, request, project_id):
        self.params = {
            "project_uuid" : project_id
        }
        role = ProjectMember.objects.filter(projectlist__uuid=project_id).get(userlist=request.user).role
        self.params["role"] = role
        return render(request, 'mainpage/project_settings_delete.html', self.params)

class ProjectSettings_delete_verification(TemplateView):
    def __init__(self):
        self.params = {}
    def get(self, request, project_id):
        self.params = {
            "project_uuid" : project_id
        }

        return render(request, 'mainpage/project_settings_delete_varification.html', self.params)

class ProjectSettings_delete_complete(TemplateView):
    def get(self, request, project_id):
        project = Project.objects.get(uuid=project_id)
        project.delete()
        return render(request, 'mainpage/project_settings_delete_complete.html')