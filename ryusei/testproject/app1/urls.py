from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("toppage/", views.index, name="app1_toppage"),
    path("page1/", views.page1, name="app1_page1"),
    path("page2/", views.page2, name="app1_page2"),
]