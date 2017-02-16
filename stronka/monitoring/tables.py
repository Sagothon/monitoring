import django_tables2 as tables
from .models import Device

class DevicesTable(tables.Table):
    class Meta:
        model = Device
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        exclude = {'port', 'password', 'login', 'id'}