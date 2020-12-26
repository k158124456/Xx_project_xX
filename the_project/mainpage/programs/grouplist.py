from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite, Status_detail
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import InviteForm


class GroupList(TemplateView):
    def __init__(self):
        
        params = {
            "userdata" : "",
            "project" : ""
        }
    def get(self, request, project_id):
        #ログインユーザーが所属しているプロジェクトを全て格納
        projects = ProjectMember.objects.filter(userlist=request.user)
        #クエリパラメータで指定されたプロジェクトが持っているグループを表示したい
        #project_id = UUID
        #グループDBの中から、プロジェクトIDのUUIDがクエリパラメータで指定されたUUIDに一致するもをフィルタ
        
        # DBへの接続回数を抑えるため、インスタンス作成しておく
        G = Group

        groups = G.objects.filter(project_id__uuid=project_id)
        selected_project = projects.get(projectlist__uuid=project_id)
        # admin_or_notにはグループ作成権限があるかどうかを指定
        admin_or_not = selected_project.role
        
        #projectメンバーの状態を取得したい
        ##とりあえず、プロジェクトに存在するグループリストを取得
        group_list = G.objects.filter(project_id__uuid=project_id)
        ##どうやってここからステータスのリストを持ってこようか
        ##リストに足してあげるといけるのかよ。
        status_lists = []
        detail_lists=[]
        for group in group_list:
            status_lists.append(Status.objects.filter(group_id=group.uuid))
            detail_lists.append(Status_detail.objects.filter(group_id=group.uuid))
        #status_detailがプロジェクト単位になってるのに疑問
    
        return_status_list = []

        name = ProjectMember.objects.filter(projectlist__uuid=project_id)

        #status：名前とステータス番号の列
        for status,detail_list in zip(status_lists,detail_lists):
            g_status_list=[]
            #for status in status_list:
            #count=1
            #status_list_=[]
            #while True:
            #    if detail_list.filter(status_id=count).exists():#status存在確認
            #        if status.filter(status=count).exists():
            #            status_list_.append(status.filter(status=count))
            #        count+=1
            #    else:break
            #status_list_=list(reversed(status_list_))#逆順のリスト

            status_list=[]
            for detail in detail_list:

                if status.filter(status=detail.status_id).exists() and detail.status_id!=0:
                    status_list.append(status.filter(status=detail.status_id))
            status_list_=list(reversed(status_list))#逆順のリスト

            for statuss_ in status_list_:
                for status_ in statuss_:
                    g_status_list.append({"name":name.get(userlist=status_.userlist).displayname, "status":detail_list.get(status_id=status_.status).detail})
            return_status_list.append(g_status_list)


            #    if status.status != 0:
            #        for detail in detail_list:
            #            if status.status == detail.status_id:
            #                g_status_list.append({"name":name.get(userlist=status.userlist).displayname, "status":detail.detail})
            #return_status_list.append(g_status_list)



        
            
            
        #test_list = [{"a":0,"b":1},{"a":0,"b":1},{"a":0,"b":1},{"a":0,"b":1}]



 
        #params["project_name"]には
        params = {
            "userdata" : str(request.user),
            "projects" : projects,
            "groups" : groups,
            "selected_project" : selected_project,
            "project_uuid" : project_id,
            "admin_or_not" : admin_or_not,
            #"member_list" : status_list,
            "status_list" : return_status_list,
        }
        return render(request, 'mainpage/grouppage.html', params)
