from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from mainpage.models import Project, Group, ProjectMember, Status, Invite,Chat,Status_detail
import pandas as pd
from django.http import HttpResponse
from ..forms import ChatForm
from django.utils import timezone
from django.contrib.auth.models import User


class Group_settings(TemplateView):
    def __init__(self):

        self.params = {
            #"form" : ChatForm()["chat_messeage"],
            "userdata" : "",
            "project" : "",
        }
    
    def get(self,request,project_id,group_id):
        groupID = group_id
        projectID = project_id
        
        #インスタンス
        group = Group.objects.get(uuid=groupID)
        status = Status.objects.filter(group_id__uuid=groupID)
        project = Project.objects.get(uuid=projectID)
        chat = Chat.objects.filter(group_id__uuid=groupID)
        groupname = group.group_name
        projectname=project.project_name
        status_detail = Status_detail.objects.filter(group_id__uuid=groupID)

        d_r=ProjectMember.objects.filter(projectlist=project).filter(userlist=request.user)

        self.params["projectmembers"] = ProjectMember.objects.filter(projectlist=project)
        self.params["projectid"] = projectID
        self.params["statuses"] = status
        self.params["groupname"] = groupname
        self.params["projectname"]=projectname
        self.params["chats"] = chat
        self.params["group"] = group
        self.params["status_details"] = status_detail
        self.params["displayname_role"] = d_r[0]
        self.params["title"]=projectname+"/"+groupname+":setting"
        self.params["projects"] = ProjectMember.objects.filter(userlist=request.user)
        

        return render(request, 'grouppage/group_settings.html', self.params)
    
    def post(self,request,project_id,group_id):
        groupID = group_id
        projectID = project_id

        #インスタンス
        group = Group.objects.get(uuid=groupID)
        status = Status.objects.filter(group_id__uuid=groupID)
        project = Project.objects.get(uuid=projectID)
        chat = Chat.objects.filter(group_id__uuid=groupID)
        status_detail = Status_detail.objects.filter(group_id__uuid=groupID)
        

        
        #chat_messeage = request.POST.get("chat_messeage")
        #record_chat = Chat(
        #    group_id = Group.objects.get(uuid=groupID),
        #    userlist = request.user,
        #    datetime = timezone.datetime.now(),
        #    chat_messeage = chat_messeage
        #)
        #record_chat.save()

        chat = Chat.objects.filter(group_id__uuid=groupID)

        d_r=ProjectMember.objects.filter(projectlist=project).filter(userlist=request.user)

        groupname = group.group_name
        self.params["projectmembers"] = ProjectMember.objects.filter(projectlist=project)
        self.params["projectid"] = projectID
        self.params["statuses"] = status
        self.params["groupname"] = groupname
        self.params["group"] = group
        self.params["chats"] = chat
        self.params["status_details"] = status_detail
        self.params["displayname_role"] = d_r[0]
        self.params["projects"] = ProjectMember.objects.filter(userlist=request.user)


        return render(request, 'grouppage/group_settings.html', self.params)




# Create your views here.
