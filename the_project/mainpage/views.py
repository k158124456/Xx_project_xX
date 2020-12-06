from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Project, Group, ProjectMember, Status, Invite
import pandas as pd
from django.http import HttpResponse
from .forms import InviteForm

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
    def get(self, request, project_id):
        #ログインユーザーが所属しているプロジェクトのメンバーを表示
        projects = ProjectMember.objects.filter(userlist=request.user)
        #クエリパラメータで指定されたプロジェクトが持っているグループを表示したい
        ## プロジェクトIDで絞るとすると、番号が必要だが、クエリパラメータには名前しか入れていないので検索できない。
        ## しかし、下記のように__で繋げてあげることによって親クラスの項目を検索することができる
        # groupsにはクエリパラメータで指定されたプロジェクトの中にあるグループを格納
        groups = Group.objects.filter(project_id__project_name=project_id)
        # admin_or_notにはグループ作成権限があるかどうかを指定
        admin_or_not = projects.filter(projectlist__project_name=project_id)[0].role
        

        params = {
            "userdata" : str(request.user),
            "project" : projects,
            "groups" : groups,
            "project_name" : project_id,
            "admin_or_not" : admin_or_not,
        }
        return render(request, 'mainpage/grouppage.html', params)

#招待したいユーザーを検索 → 検索に合致するユーザーがいたらその人を選択 → messageを入力して招待を送信
class InviteMembers(TemplateView):
    def get(self, request, project_id):
        self.params = {
            "project_name" : "" ,
            "form_serch_user" : InviteForm()["invited_user"],
            "form_message" : InviteForm()["message"],
            "degug" : [],
            "message" : "",
        }
        self.params["project_name"] = project_id

        # クエリパラメータ(?usr=<username>)で指定されたusernameをinvite_userに格納
        self.invite_user = request.GET["usr"]
        # クエリパラメータで指定されているプロジェクトネームを格納
        self.invited_project = self.params["project_name"]

        return render(request, 'mainpage/invite.html', self.params)

    def post(self, request):
        # フォームから入力された各値を格納
        self.message = request.POST.get("message")
        self.invited_user = request.POST.get("invited_user")
        
        #データベースに格納
        iv = Invite(
            project_name=self.invited_project, 
            invite_user=self.invite_user, 
            invited_user=self.invited_user,
            message=self.message
            )
        iv.save()

        self.params["message"] = "招待メッセージを送りました。"

        return render(request, "mainpage/invite.html", self.params)
        
        




        

    


        return render(request, 'mainpage/invite.html')

class CreateGroup(TemplateView):
    def get(self, request, project_id):
        params = {
            "project_name" : "" 
        }
        params["project_name"] = project_id
        return render(request, 'mainpage/create.html', params)
    def post(self, request):
        return render(request, 'mainpage/create.html')


