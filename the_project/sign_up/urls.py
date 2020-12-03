from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'sign_up'
urlpatterns = [
    path('', views.SignUp.as_view(), name='sign_up_page'),
    path('complete/',views.comp, name="sign_up_completed")
    
]