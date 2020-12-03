from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required


class MainPage(TemplateView):
    def get(self, request):
        return render(request, 'mainpage/mainpage.html')