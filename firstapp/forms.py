from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()
    ratio = forms.CharField()

class SecretForm(forms.Form):
    mas = forms.CharField()
