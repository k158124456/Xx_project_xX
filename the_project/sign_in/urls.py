from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'sign_in'

urlpatterns = [
    path('', views.Login.as_view(), name='sign_in'),
    path('sign_out/', views.Logout.as_view(), name='sign_out'),
    path('sign_out_page',views.logout, name='sign_out_page')


]