from django.shortcuts import render
from .models import Device
from django.shortcuts import render
from django_tables2 import RequestConfig
from .tables import DevicesTable

# Create your views here.
#def device_list(request):
#    devices = Device.objects.all()
#    return render(request, 'monitoring/device_list.html', {'devices': devices})

def dev_table(request):
    table = DevicesTable(Device.objects.all())
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=500)
    return render(request, 'monitoring/device_list.html', {'table': table})