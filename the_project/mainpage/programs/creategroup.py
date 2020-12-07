from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import InviteForm

class CreateGroup(TemplateView):
    def get(self, request, project_id):
        params = {
            "project_name" : "" 
        }
        params["project_name"] = project_id
        return render(request, 'mainpage/create.html', params)
    def post(self, request):
        return render(request, 'mainpage/create.html')
