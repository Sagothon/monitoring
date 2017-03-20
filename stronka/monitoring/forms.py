from django import forms

class ConfigForm(forms.Form):
    ip = forms.CharField(max_length=100)
    