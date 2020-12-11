from django import forms

from django.contrib.auth.forms import AuthenticationForm 

class InviteForm(forms.Form):
    message = forms.CharField(max_length=100, label='message', widget=forms.TextInput(attrs={'class':'form-controll'}))
    invited_user = forms.CharField(max_length=20, label='user name', widget=forms.TextInput(attrs={'class':'form-controll'}))

class CreateProjectForm(forms.Form):
    project_name = forms.CharField(max_length=20, label='project name', widget=forms.TextInput(attrs={'class':'form-controll'}))

class CreateGroupForm(forms.Form):
    group_name = forms.CharField(max_length=20, label='group name', widget=forms.TextInput(attrs={'class':'form-controll'}))