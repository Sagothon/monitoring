from django.shortcuts import render
from .models import Device
from django.shortcuts import render
from django_tables2 import RequestConfig
from .tables import DevicesTable
from .forms import ConfigForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import subprocess
from .lib.discover import ubnt_discovery

def pole():
    print('dfddfd')

@login_required
def dev_table(request):

    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        table = DevicesTable(Device.objects.all())
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get('page', 1), per_page=500)
        return render(request, 'monitoring/device_list.html', {'table': table})
        
@login_required
def configuration(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ubnt_discovery(data)
            return HttpResponseRedirect('/')
    else:
        form = ConfigForm()

    return render(request, 'monitoring/config.html', {'form': form})
