from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from mainpage.models import Project, Group, ProjectMember, Status, Invite,Chat,Status_detail
import pandas as pd
from django.http import HttpResponse
from ..forms import ChatForm
from django.utils import timezone
from django.contrib.auth.models import User


class RoomPage(TemplateView):
    def __init__(self):

        self.params = {
            "form" : ChatForm()["chat_messeage"],
            "userdata" : "",
            "project" : "",
        }
    
    def get(self,request,project_id,group_id):
        #groupid と　projectidを取得
        #groupID = request.GET["groupname"]
        groupID = group_id
        projectID = project_id
        
        #インスタンス取得
        group = Group.objects.get(uuid=groupID)
        status = Status.objects.filter(group_id__uuid=groupID)
        project = Project.objects.get(uuid=projectID)
        chat = Chat.objects.filter(group_id__uuid=groupID)
        groupname = group.group_name
        status_detail = Status_detail.objects.filter(group_id__uuid=groupID)
        projectname=project.project_name
        projectmember = ProjectMember.objects.filter(projectlist=project)
        d_r=projectmember.filter(userlist=request.user)
        

        if 'status' in request.GET:
            sta_list=Status.objects.filter(userlist=request.user)
            for sta in sta_list:
                sta.status=0
                sta.save()

            st=request.GET['status']
            record_status=Status.objects.get(group_id=Group.objects.get(uuid=groupID),userlist=request.user)
            record_status.status=Status_detail.objects.get(group_id__uuid=groupID,detail=st).status_id
            record_status.save()

        #status状態順→名前順？にソートする
        count=0
        status_list=[]
        while True:
            if status_detail.filter(status_id=count).exists():#status存在確認
                if status.filter(status=count).exists():
                    status_list.append(status.filter(status=count))
                count+=1
            else:break
        status_list=list(reversed(status_list))#逆順のリスト
        #------

        #{権限持っているか, 名前, ステータス, 書き置きコメント}の辞書を作る
        return_list = []
        for statuses in status_list:
            for status in statuses:
                status_dict = {}
                # プロジェクトでのディスプレーネームを探す
                for member in projectmember:
                    if member.userlist == status.userlist:
                        status_dict["username"] = member.displayname
                        status_dict["role"] = member.role
                        
                        for chat_ in chat:
                            if chat_.userlist == status.userlist:
                                status_dict["message"] = chat_.chat_messeage
                        

                for status_detail_ in status_detail:
                    if status.status == status_detail_.status_id:
                        status_dict["status"] = status_detail_.detail

                return_list.append(status_dict)
        

        self.params["projectmembers"] = ProjectMember.objects.filter(projectlist=project)
        self.params["projectid"] = projectID
        self.params["statuses"] = status
        self.params["groupname"] = groupname
        self.params["projectname"] = projectname
        self.params["chats"] = chat
        self.params["group"] = group
        self.params["status_details"] = status_detail
        self.params["displayname_role"] = d_r[0]
        self.params["title"]=projectname+"/"+groupname
        self.params["status_list"]=status_list
        self.params["contains"] = return_list

        





        

        return render(request, 'grouppage/roompage.html', self.params)
    
    def post(self,request,project_id,group_id):

        #groupID = request.GET["groupname"]
        groupID = group_id
        
        #groups = Group.objects.filter(project_id__uuid=project_id)
        projectID = project_id
        #groupインスタンスを取得
        group = Group.objects.get(uuid=groupID)
        status = Status.objects.filter(group_id__uuid=groupID)
        project = Project.objects.get(uuid=projectID)
        chat = Chat.objects.filter(group_id__uuid=groupID)
        status_detail = Status_detail.objects.filter(group_id__uuid=groupID)
        projectname=project.project_name
        projectmember = ProjectMember.objects.filter(projectlist=project)
        d_r=projectmember.filter(userlist=request.user)

        #status状態順→名前順？にソートする
        count=0
        status_list=[]
        while True:
            if status_detail.filter(status_id=count).exists():#status存在確認
                if status.filter(status=count).exists():
                    status_list.append(status.filter(status=count))
                count+=1
            else:break
        status_list=list(reversed(status_list))#逆順のリスト
        #------


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

        #{権限持っているか, 名前, ステータス, 書き置きコメント}の辞書を作る
        return_list = []
        for statuses in status_list:
            for status in statuses:
                status_dict = {}
                # プロジェクトでのディスプレーネームを探す
                for member in projectmember:
                    if member.userlist == status.userlist:
                        status_dict["username"] = member.displayname
                        status_dict["role"] = member.role
                        
                        for chat_ in chat:
                            if chat_.userlist == status.userlist:
                                status_dict["message"] = chat_.chat_messeage
                        

                for status_detail_ in status_detail:
                    if status.status == status_detail_.status_id:
                        status_dict["status"] = status_detail_.detail

                return_list.append(status_dict)
        

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
        self.params["title"]=projectname+"/"+groupname
        self.params["status_list"]=status_list
        self.params["contains"] = return_list


        return render(request, 'grouppage/roompage.html', self.params)




# Create your views here.
