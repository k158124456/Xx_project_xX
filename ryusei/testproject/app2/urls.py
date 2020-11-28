from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "app2"
urlpatterns = [
    path("toppage/", views.index, name="toppage"),
    path("form/", views.BmiView.as_view(), name="form")
]
