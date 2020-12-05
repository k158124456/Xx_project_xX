from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Project, Group, ProjectMember, Status
import pandas as pd
from django.http import HttpResponse

class MainPage(TemplateView):
    def get(self, request):
        projects = ProjectMember.objects.filter(userlist=request.user)

        params = {
            "userdata" : str(request.user),
            "project" : projects
        }

        return render(request, 'mainpage/mainpage.html', params)

class GroupList(TemplateView):
    def __init__(self):
        
        params = {
            "userdata" : "",
            "project" : ""
        }
    def get(self, request, id):
        #ログインユーザーが所属しているプロジェクトのメンバーを表示
        projects = ProjectMember.objects.filter(userlist=request.user)
        #クエリパラメータで指定されたプロジェクトが持っているグループを表示したい
        ## プロジェクトIDで絞るとすると、番号が必要だが、クエリパラメータには名前しか入れていないので検索できない。
        ## しかし、下記のように__で繋げてあげることによって親クラスの項目を検索することができる
        # groupsにはクエリパラメータで指定されたプロジェクトの中にあるグループを格納
        groups = Group.objects.filter(project_id__project_name=id)
        # admin_or_notにはグループ作成権限があるかどうかを指定
        admin_or_not = projects.filter(projectlist__project_name=id)[0].role
        

        params = {
            "userdata" : str(request.user),
            "project" : projects,
            "groups" : groups,
            "project_name" : id,
            "admin_or_not" : admin_or_not,
        }
        return render(request, 'mainpage/grouppage.html', params)

class RoomPage(TemplateView):
    def __init__(self):
        
        params = {
            "userdata" : "",
            "project" : "",
        }
    
    def get(self,request,id,group_name):
        projects = ProjectMember.objects.filter(userlist=request.user)
        groups = Group.objects.filter(project_id__project_name=id)
        admin_or_not = projects.filter(projectlist__project_name=id)[0].role
        statuss = Status.objects.filter(group_id__group_name=group_name)
        
        params = {
            "userdata" : str(request.user),
            "project" : projects,
            "groups" : groups,
            "project_name" : id,
            "admin_or_not" : admin_or_not,
            "statuss" : statuss,
            "group_name" : group_name,
            
        }
        return render(request, 'mainpage/roompage.html', params)



