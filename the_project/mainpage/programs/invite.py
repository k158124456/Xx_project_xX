from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import InviteForm

#招待したいユーザーを検索 → 検索に合致するユーザーがいたらその人を選択 → messageを入力して招待を送信
class InviteMembers(TemplateView):
    def __init__(self):
        self.params = {
            "project_name" : "" ,
            "form_serch_user" : InviteForm()["invited_user"],
            "form_message" : InviteForm()["message"],
            "degug" : [],
            "message" : "",
            "usr" : "",
            "msg":""
        }
    ################################################################################
    ###処理で用いる関数たち
    #すでにIDが存在しているかの判定
    def exist_id(self, userid):
        #IDで元DBを検索かけて中身が存在しなければFalseを返す
        user_id = User.objects.filter(username=userid)
        #これはクエリーセットを返しているけれど、クエリーセットは中身があればそれはTrue要素を含んでいるらしい
        return user_id
    #自分自身に招待を送った場合(同じ場合False、異なる場合True)
    def owner(self, userid):
        return userid != self.params["usr"]

    #招待するユーザがすでにprojectに参加しているかどうかの判別を行う関数
    def check_recorded(self, invited_id, project_id):
        isin_Project = ProjectMember.objects.filter(
                            projectlist__uuid=project_id
                            ).filter(
                                userlist__username=invited_id
                            )
        return isin_Project

    #################################################################################

    def get(self, request, project_id):
        self.params["projects"] = ProjectMember.objects.filter(userlist=request.user)
        self.params["usr"] = request.GET["usr"]
        self.params["project"] = Project.objects.get(uuid=project_id)

        # クエリパラメータ(?usr=<username>)で指定されたusernameをinvite_userに格納
        self.invite_user = request.GET["usr"]
        # クエリパラメータで指定されているプロジェクトネームを格納
        self.invited_project = self.params["project"]

        return render(request, 'mainpage/invite.html', self.params)

    def post(self, request, project_id):
        # フォームから入力された各値を格納
        self.params["projects"] = ProjectMember.objects.filter(userlist=request.user)
        self.params["usr"] = request.GET["usr"]
        self.params["project"] = Project.objects.get(uuid=project_id)
        self.message = request.POST.get("message")
        self.invited_user = request.POST.get("invited_user")
        self.invite_user = self.params["usr"]
        self.invited_project = self.params["project"]

        
        

        #登録できるか否か(Trueで登録可能、Falseで登録不可能)
        exist_ornot = self.exist_id(self.invited_user)
        owner_ornot = self.owner(self.invited_user)
        already_recorded = not(self.check_recorded(self.invited_user, project_id))

        recordable = exist_ornot and owner_ornot and already_recorded
        #recordable = False
        self.params["debug"] = owner_ornot

        if recordable:
            iv = Invite(
                
                invite_user=User.objects.get(username=self.invite_user), 
                invited_user=User.objects.get(username=self.invited_user),
                project_name=Project.objects.get(uuid=project_id),
                message=self.message,
                )
            iv.save()
            self.params["message"] = "招待メッセージを送りました。"
            return render(request, "mainpage/invite_comp.html", self.params)
        else:
            if not(exist_ornot):
                self.params["msg"] += "<br>そのようなユーザーIDは存在しません"

            if not(owner_ornot):
                self.params["msg"] += "<br>自分自身を招待することはできません"
            
            if not(already_recorded):
                self.params["msg"] += "<br>招待したユーザーはすでにこのプロジェクトに参加しています"

            self.params["msg"] = self.params["msg"][4:]
            self.params["form_message"] = InviteForm(request.POST)["message"]
            return render(request, "mainpage/invite.html", self.params)
