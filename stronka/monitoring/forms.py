from django import forms

class ConfigForm(forms.Form):
    ip = forms.CharField(max_length=100)
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    port = forms.CharField(max_length=100)

class CronForm(forms.Form):
    monitor_minutes = forms.CharField(max_length=100)
    ping_check = forms.CharField(max_length=100)
    backup_days = forms.CharField(max_length=100)

class MailForm(forms.Form):
    mail_to = forms.CharField(max_length=100)