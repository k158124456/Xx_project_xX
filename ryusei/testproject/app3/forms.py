from django import forms

class IdForm(forms.Form):
    id = forms.IntegerField(label='id', widget=forms.NumberInput(attrs={'class':'form-controll'}))
