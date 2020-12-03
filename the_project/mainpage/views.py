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
        groups = Group.objects.filter(project_id=1)
        params = {
            "userdata" : str(request.user),
            "project" : projects,
            "groups" : groups,
            "project_name" : id
        }
        return render(request, 'mainpage/grouppage.html', params)