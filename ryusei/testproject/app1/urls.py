from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "app1"
urlpatterns = [
    path("toppage/", views.index, name="toppage"),
    path("page1/", views.page1, name="page1"),
    path("page2/", views.page2, name="page2"),
]