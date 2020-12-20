from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite,Status_detail
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import CreateGroupForm

class CreateGroup(TemplateView):
    def __init__(self):
        self.params = {
            "form" : CreateGroupForm()["group_name"],
            "group_name" : ""
        }
    def get(self, request, project_id):

        self.params["project_name"] = project_id
        return render(request, 'mainpage/creategroup.html', self.params)

    def post(self, request, project_id):
        self.params["project_name"] = project_id
        group_name = request.POST.get("group_name")
        project_id = project_id


        recordable = True

        if recordable:
            group = Group(
                project_id = Project.objects.get(uuid=project_id),
                group_name=group_name,
            )
            group.save()
            #ステータスにグループ、メンバー、ステータスを追加する
            ##まず、プロジェクトに所属している人間を取得
            project_member = ProjectMember.objects.filter(
                projectlist__uuid=project_id
            )
            for member in project_member:
                record_status = Status(
                    userlist=User.objects.get(username=member.userlist),
                    group_id=Group.objects.get(uuid=group.uuid),
                    status=0
                )
                record_status.save()
            
            sd = Status_detail(
                group_id=Group.objects.get(uuid=group.uuid),
                status_id = 0,
                detail = "オフライン",
            )
            sd.save()
            sd = Status_detail(
                group_id=Group.objects.get(uuid=group.uuid),
                status_id = 1,
                detail = "オンライン",
            )
            sd.save()

            return render(request, 'mainpage/creategroup.html', self.params)

