from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite, Status_detail
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import InviteForm

class Leave(TemplateView):
    def get(self, request):
        user = request.user
        projects = ProjectMember.objects.filter(userlist=user)

        for project in projects:
            groups = Group.objects.filter(project_id=project.projectlist.uuid)
            
            for group in groups:
                statuses = Status.objects.filter(group_id=group.uuid).filter(userlist=user)
                
                for status in statuses:
                    status.status = 0
                    status.save()
                




            

        return redirect('/mainpage')