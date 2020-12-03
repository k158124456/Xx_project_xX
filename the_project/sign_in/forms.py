from django import forms

<<<<<<< HEAD
class TestForm(forms.Form):
    text = forms.CharField(label='文字入力')
    num = forms.IntegerField(label='数量')
=======
from django.contrib.auth.forms import AuthenticationForm 


class LoginForm(AuthenticationForm):
    """ログオンフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
>>>>>>> 3a9af7aea28b2e4287054be6d6817184c1343269
