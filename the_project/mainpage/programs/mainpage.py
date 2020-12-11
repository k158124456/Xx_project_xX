from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import InviteForm

class MainPage(TemplateView):
    def get(self, request):
        projects = ProjectMember.objects.filter(userlist=request.user)

        params = {
            "userdata" : str(request.user),
            "projects" : projects
        }

        return render(request, 'mainpage/mainpage.html', params)
