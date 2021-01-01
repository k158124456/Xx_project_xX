from django import forms
from django.contrib.auth.forms import AuthenticationForm 


class ChatForm(forms.Form):
    chat_messeage = forms.CharField(max_length=1000, label='chat', widget=forms.TextInput(attrs={'class':'form-control'}))

class StatusForm(forms.Form):
    detail = forms.CharField(max_length=10, label='sta', widget=forms.TextInput(attrs={'class':'form-control'}))

class GroupNameForm(forms.Form):
    name=forms.CharField(max_length=100,label='name',widget=forms.TextInput(attrs={'class':'form-control'}))