from django import forms

class BmiForm(forms.Form):
    hight = forms.FloatField(label="hight", widget=forms.NumberInput(attrs={'class':'form-controll'}))
    weight = forms.FloatField(label="weight", widget=forms.NumberInput(attrs={'class':'form-controll'}))
    