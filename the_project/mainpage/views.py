from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Project, Group, ProjectMember, Status

class MainPage(TemplateView):
    def get(self, request):
        projects = ProjectMember.objects.filter(userlist='test_1')
        params = {
            "userdata" : str(request.user),
            "projects" : projects
        }
        return render(request, 'mainpage/mainpage.html', params)