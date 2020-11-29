from django import forms

class SignupForm(forms.Form):
    user_id = forms.CharField(max_length=20, label='user id', widget=forms.TextInput(attrs={'class':'form-controll'}))
    mail = forms.EmailField(max_length=100, label='mail', widget=forms.TextInput(attrs={'class':'form-controll'}))
    pswd = forms.CharField(max_length=20, label='psssword', widget=forms.PasswordInput(attrs={'class':'form-controll'}))
    re_pswd = forms.CharField(max_length=20,label='もう一度入力', widget=forms.PasswordInput(attrs={'class':'form-controll'}))