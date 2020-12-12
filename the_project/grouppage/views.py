from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from mainpage.models import Project, Group, ProjectMember, Status, Invite,Chat
import pandas as pd
from django.http import HttpResponse
from .forms import ChatForm
from django.utils import timezone
from django.contrib.auth.models import User


class RoomPage(TemplateView):
    def __init__(self):

        self.params = {
            "form" : ChatForm()["chat_messeage"],
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
        self.params["group"] = group

        

        return render(request, 'grouppage/roompage.html', self.params)
    
    def post(self,request,project_id):

        groupID = request.GET["groupname"]
        
        #groups = Group.objects.filter(project_id__uuid=project_id)
        projectID = project_id
        #groupインスタンスを取得
        group = Group.objects.get(uuid=groupID)
        status = Status.objects.filter(group_id__uuid=groupID)
        project = Project.objects.get(uuid=projectID)
        chat = Chat.objects.filter(group_id__uuid=groupID)
        

        
        chat_messeage = request.POST.get("chat_messeage")
        #groupID = request.GET["groupname"]
        projectID = project_id
        record_chat = Chat(
            group_id = Group.objects.get(uuid=groupID),
            userlist = request.user,
            datetime = timezone.datetime.now(),
            chat_messeage = chat_messeage
        )
        record_chat.save()

        chat = Chat.objects.filter(group_id__uuid=groupID)

        groupname = group.group_name
        self.params["projectmembers"] = ProjectMember.objects.filter(projectlist=project)
        self.params["projectid"] = projectID
        self.params["statuses"] = status
        self.params["groupname"] = groupname
        self.params["group"] = group
        self.params["chats"] = chat


        return render(request, 'grouppage/roompage.html', self.params)




# Create your views here.
