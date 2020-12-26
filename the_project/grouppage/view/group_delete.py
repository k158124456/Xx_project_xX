from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from mainpage.models import *
import pandas as pd
from django.http import HttpResponse
from ..forms import *
from django.utils import timezone
from django.contrib.auth.models import User


class Group_Delete(TemplateView):
    def __init__(self):

        self.params = {
            "userdata" : "",
            "project" : "",
        }
    
    def get(self,request,project_id,group_id):
        #groupid と　projectidを取得
        groupID = group_id#request.GET["groupname"]
        projectID = project_id
        
        #groupインスタンスを取得
        group = Group.objects.get(uuid=groupID)
        status = Status.objects.filter(group_id__uuid=groupID)
        project = Project.objects.get(uuid=projectID)
        chat = Chat.objects.filter(group_id__uuid=groupID)
        groupname = group.group_name
        status_detail = Status_detail.objects.filter(group_id__uuid=groupID)
        projectname=project.project_name

        d_r=ProjectMember.objects.filter(projectlist=project).filter(userlist=request.user)

        self.params["projectmembers"] = ProjectMember.objects.filter(projectlist=project)
        self.params["projectid"] = projectID
        self.params["statuses"] = status
        self.params["groupname"] = groupname
        self.params["projectname"] = projectname
        self.params["chats"] = chat
        self.params["group"] = group
        self.params["status_details"] = status_detail
        self.params["displayname_role"] = d_r[0]
        self.params["title"]=projectname+"/"+groupname+":setting_group_detele"

        

        return render(request, 'grouppage/group_delete.html', self.params)


class Group_Delete_Complete(TemplateView):
    def __init__(self):

        self.params = {
            "userdata" : "",
            "project" : "",
        }
    
    def get(self,request,project_id,group_id):
        #groupid と　projectidを取得
        groupID = group_id#request.GET["groupname"]
        projectID = project_id
        
        #インスタンス取得
        group = Group.objects.get(uuid=groupID)
        project = Project.objects.get(uuid=projectID)
        projectname=project.project_name
        groupname = group.group_name
        d_r=ProjectMember.objects.filter(projectlist=project).filter(userlist=request.user)
        group.delete()


        self.params["projectmembers"] = ProjectMember.objects.filter(projectlist=project)
        self.params["projectid"] = projectID
        self.params["projectname"] = projectname
        self.params["groupname"] = groupname
        self.params["displayname_role"] = d_r[0]
        self.params["title"]=projectname+"/"+groupname+":setting_group_detele_complete"

        

        return render(request, 'grouppage/group_delete_complete.html', self.params)



# Create your views here.
