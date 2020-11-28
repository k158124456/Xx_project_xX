from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'sign_up'
urlpatterns = [
    path('', views.index, name='sign_up_page')
]