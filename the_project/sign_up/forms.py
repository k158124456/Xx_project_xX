from django import forms

class SignupForm(forms.Form):
    user_id = forms.CharField(max_length=20, label='user_id', widget=forms.TextInput(attrs={'class':'form-controll'}))
    mail = forms.EmailField(max_length=100, label='mail', widget=forms.TextInput(attrs={'class':'form-controll'}))
    pswd = forms.CharField(max_length=20, label='pswd', widget=forms.PasswordInput(attrs={'class':'form-controll'}))
    retype_pswd = forms.CharField(max_length=20,label='re_pswd', widget=forms.PasswordInput(attrs={'class':'form-controll'}))