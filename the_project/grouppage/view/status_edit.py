from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from mainpage.models import *
import pandas as pd
from django.http import HttpResponse
from ..forms import *
from django.utils import timezone
from django.contrib.auth.models import User


class Status_new(TemplateView):
    def __init__(self):

        self.params = {
            "form" : StatusForm()["detail"],
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

        if "target" in request.GET:
            target=request.GET['target']
            mode=request.GET['mode']
            detail=status_detail.get(status_id=target)
            statuss=status.filter(status=target)

            if mode=="delete":
                detail.delete()
                for status_ in statuss:
                    status_.status=0
                    status_.save()



        self.params["projectmembers"] = ProjectMember.objects.filter(projectlist=project)
        self.params["projectid"] = projectID
        self.params["statuses"] = status
        self.params["groupname"] = groupname
        self.params["projectname"] = projectname
        self.params["chats"] = chat
        self.params["group"] = group
        self.params["status_details"] = status_detail
        self.params["displayname_role"] = d_r[0]
        self.params["title"]=projectname+"/"+groupname+":setting_status_edit"

        

        return render(request, 'grouppage/status_edit.html', self.params)
    
    def post(self,request,project_id,group_id):

        groupID = group_id#request.GET["groupname"]
        
        #groups = Group.objects.filter(project_id__uuid=project_id)
        projectID = project_id
        #groupインスタンスを取得
        group = Group.objects.get(uuid=groupID)
        status = Status.objects.filter(group_id__uuid=groupID)
        project = Project.objects.get(uuid=projectID)
        chat = Chat.objects.filter(group_id__uuid=groupID)
        status_detail = Status_detail.objects.filter(group_id__uuid=groupID)
        projectname=project.project_name
        

        status_id_new=status_detail.order_by('-status_id')[0]
        
        status_new = request.POST.get("detail")
        #groupID = request.GET["groupname"]
        projectID = project_id
        record_status = Status_detail(
            group_id=group,
            status_id=1+status_id_new.status_id,
            detail=status_new,
        )
        record_status.save()

        chat = Chat.objects.filter(group_id__uuid=groupID)

        d_r=ProjectMember.objects.filter(projectlist=project).filter(userlist=request.user)

        groupname = group.group_name
        self.params["projectmembers"] = ProjectMember.objects.filter(projectlist=project)
        self.params["projectid"] = projectID
        self.params["statuses"] = status
        self.params["groupname"] = groupname
        self.params["projectname"] = projectname
        self.params["group"] = group
        self.params["chats"] = chat
        self.params["status_details"] = status_detail
        self.params["displayname_role"] = d_r[0]
        self.params["title"]=projectname+"/"+groupname+":setting_status_edit"


        return render(request, 'grouppage/status_edit.html', self.params)




# Create your views here.
