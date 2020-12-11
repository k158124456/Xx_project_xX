from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from mainpage.models import Project, Group, ProjectMember, Status, Invite
import pandas as pd
from django.http import HttpResponse
from mainpage.forms import InviteForm


class RoomPage(TemplateView):
    def __init__(self):
        
        self.params = {
            "userdata" : "",
            "project" : "",
        }
    
    def get(self,request,project_id):
        #groupid と　projectidを取得
        groupID = request.GET["groupname"]
        projectID = project_id
        
        #groupインスタンスを取得
        group = Group.objects.get(uuid=groupID)
        status = Status.objects.filter(group_id__uuid=groupID)

        groupname = group.group_name
        self.params["statuses"] = status
        self.params["groupname"] = groupname
        self.params["projectid"] = projectID

        return render(request, 'grouppage/roompage.html', self.params)


# Create your views here.
