from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite
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
        

        groups = Group.objects.filter(project_id__uuid=project_id)
        selected_project = projects.get(projectlist__uuid=project_id)
        # admin_or_notにはグループ作成権限があるかどうかを指定
        admin_or_not = selected_project.role
        
        #params["project_name"]には
        params = {
            "userdata" : str(request.user),
            "projects" : projects,
            "groups" : groups,
            "selected_project" : selected_project,
            "project_uuid" : project_id,
            "admin_or_not" : admin_or_not,
        }
        return render(request, 'mainpage/grouppage.html', params)
