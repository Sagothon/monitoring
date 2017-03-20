from django.shortcuts import render
from .models import Device
from django.shortcuts import render
from django_tables2 import RequestConfig
from .tables import DevicesTable
from .forms import ConfigForm
from django.http import HttpResponseRedirect

def dev_table(request):

    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        table = DevicesTable(Device.objects.all())
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get('page', 1), per_page=500)
        return render(request, 'monitoring/device_list.html', {'table': table})

def configuration(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = ConfigForm()

    return render(request, 'monitoring/config.html', {'form': form})
