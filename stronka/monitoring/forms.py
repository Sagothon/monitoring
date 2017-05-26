from django import forms

class ConfigForm(forms.Form):
    ip = forms.CharField(max_length=100)
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    port = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)
        self.fields['ip'].label = "adres sieci"
        self.fields['login'].label = "domyślny login"
        self.fields['password'].label = 'domyślne hasło'
        self.fields['port'].label = "port SSH"

class CronForm(forms.Form):
    monitor_minutes = forms.CharField(max_length=100)
    ping_check = forms.CharField(max_length=100)
    backup_days = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(CronForm, self).__init__(*args, **kwargs)
        self.fields['monitor_minutes'].label = "czas monitorowania"
        self.fields['ping_check'].label = "czas pingowania"
        self.fields['backup_days'].label = "dni backupu"

class MailForm(forms.Form):
    mail_to = forms.CharField(max_length=100)