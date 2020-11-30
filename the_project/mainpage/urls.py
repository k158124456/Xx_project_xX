from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('', views.MainPage.as_view(), name='mainpage'),
]