from django import forms

class ConfigForm(forms.Form):
    ip = forms.CharField(max_length=100)
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    port = forms.CharField(max_length=100)
