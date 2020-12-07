from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from ..models import Project, Group, ProjectMember, Status, Invite
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
from ..forms import InviteForm

class Notify(TemplateView):
    def get(self, request):
        notify_list = Invite.objects.filter(invited_user=request.user)
        projects = ProjectMember.objects.filter(userlist=request.user)

        params = {
            "userdata" : str(request.user),
            "items" : notify_list
        }

        return render(request, 'mainpage/notify.html', params)