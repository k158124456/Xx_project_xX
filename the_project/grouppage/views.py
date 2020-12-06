from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from mainpage.models import Project, Group, ProjectMember, Status, Invite
import pandas as pd
from django.http import HttpResponse
from mainpage.forms import InviteForm


class RoomPage(TemplateView):
    def __init__(self):
        
        params = {
            "userdata" : "",
            "project" : "",
        }
    
    def get(self,request,project_id):
        projects = ProjectMember.objects.filter(userlist=request.user)
        groups = Group.objects.filter(project_id__project_name=project_id)
        admin_or_not = projects.filter(projectlist__project_name=project_id)[0].role
        statuss = Status.objects.filter(group_id__group_name=request.GET["groupname"])
        
        params = {
            "userdata" : str(request.user),
            "project" : projects,
            "groups" : groups,
            "project_name" : project_id,
            "admin_or_not" : admin_or_not,
            "statuss" : statuss,
            "group_name" : "group_name",
            
        }
        return render(request, 'grouppage/roompage.html', params)


# Create your views here.
