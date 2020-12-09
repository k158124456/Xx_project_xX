from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import InviteForm
from django.urls import reverse
from urllib.parse import urlencode

class Notify(TemplateView):
    def get(self, request):
        notify_list = Invite.objects.filter(invited_user=request.user)
        projects = ProjectMember.objects.filter(userlist=request.user)

        params = {
            "userdata" : str(request.user),
            "items" : notify_list,
            "message":""
        }
        # リダイレクトされた時に一緒に渡されたクエリパラメータから判断
        if 'a_project' in request.GET:
            params["message"] = request.GET["a_project"] + "に加入しました"
        if 'd_project' in request.GET:
            params["message"] = request.GET["d_project"] + "への招待を全て拒否しました"
        if 'message' in request.GET:
            params["message"] = request.GET["message"] + "にはすでに加入しています。招待を削除しました"
        
        
        return render(request, 'mainpage/notify.html', params)

class Accept(TemplateView):
    def get(self, request):
        #パラメータのprojectを読み取り
        projectname = request.GET['project']
        #projectメンバの中で、招待されているprojectでフィルタし、その上でログインユーザでフィルタリングした時に、中に何も入っていなければ登録される
        already_recorded = ProjectMember.objects.filter(
            projectlist=Project.objects.get(project_name=projectname)
            ).filter(userlist=request.user)
        
        #存在しているかどうか
        recordable = already_recorded
        #存在しているのであれば、招待されているものを全て消去
        if recordable:
            inv = Invite.objects.filter(
                project_name=Project.objects.get(project_name=projectname)
                )
            inv.delete()
            redirect_url = reverse('mainpage:notify')
            return redirect(redirect_url+"?message="+projectname)

        #存在しない場合、projectメンバーとして登録される
        else:
            pm = ProjectMember(
                userlist = request.user,
                projectlist = Project.objects.get(project_name=projectname),
                displayname = "新参者",
                role = 0,
            )
            pm.save()

            #招待されているものを削除
            inv = Invite.objects.filter(
                project_name=Project.objects.get(project_name=projectname)
                )
            inv.delete()

            redirect_url = reverse('mainpage:notify')
            return redirect(redirect_url+"?a_project="+projectname)

class Reject(TemplateView):
    def get(self, request):
        redirect_url = reverse('mainpage:notify')
        projectname = request.GET['project']
        inv = Invite.objects.filter(
            project_name=Project.objects.get(project_name=projectname)
            )
        inv.delete()

        return redirect(redirect_url+"?d_project="+projectname)
