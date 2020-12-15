from django import forms
from django.contrib.auth.forms import AuthenticationForm 


class ChatForm(forms.Form):
    chat_messeage = forms.CharField(max_length=1000, label='chat', widget=forms.Textarea(attrs={'class':'form-controll'}))