import django_tables2 as tables
from .models import Device
from django.utils.safestring import mark_safe

class CustomCheckBoxColumn(tables.CheckBoxColumn):
    def render(self, value, record, bound_column):
        box = '<input value="%s", type="checkbox", name="cBox[]"/><a href="http://%s"> %s</a>' %(value, value, value)
        return mark_safe(box)

class DevicesTable(tables.Table):
    ip = CustomCheckBoxColumn()
    class Meta:
        model = Device
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        exclude = {'port', 'password', 'login', 'ssid', 'air_q', 'air_c', 'ping', 'freq'}
