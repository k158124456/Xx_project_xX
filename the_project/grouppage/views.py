from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from mainpage.models import Project, Group, ProjectMember, Status, Invite,Chat
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
        project = Project.objects.get(uuid=projectID)
        chat = Chat.objects.filter(group_id__uuid=groupID)
        self.params["projectmembers"] = ProjectMember.objects.filter(projectlist=project)

        groupname = group.group_name
        self.params["projectid"] = projectID
        self.params["statuses"] = status
        self.params["groupname"] = groupname
        self.params["chats"] = chat

        

        return render(request, 'grouppage/roompage.html', self.params)


# Create your views here.
