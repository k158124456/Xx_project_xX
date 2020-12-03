from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'app3'

urlpatterns = [
    path("toppage/", views.index, name="toppage"),
]