from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'toppage'
urlpatterns = [
    path('', views.index, name='toppage'),
    
]