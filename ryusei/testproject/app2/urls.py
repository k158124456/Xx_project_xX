from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("toppage", view.index, name='app1_toppage')
]