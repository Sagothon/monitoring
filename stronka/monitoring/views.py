from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Device
from django.shortcuts import render
from django_tables2 import RequestConfig
from .tables import DevicesTable
from .forms import ConfigForm
from .forms import CronForm, MailForm
from .lib.discover import ubnt_discovery
from .lib.ping import ping
from .lib.update import update
import sqlite3
import subprocess
import os
from crontab import CronTab

@login_required
def dev_table(request):
    if request.POST.get("Update"):
        update(request.POST.getlist('cBox[]'))
        return HttpResponseRedirect('/')
    if request.POST.get("check"):
        ping()
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

@login_required
def cron(request):
    if request.method == 'POST':
        cron_form = CronForm(request.POST)
        if cron_form.is_valid():
            data = cron_form.cleaned_data
            print(data)
            users_cron = CronTab(user='karol')
            users_cron.remove_all()

            monit_job = users_cron.new(command='/usr/bin/python3 %s/monitoring/lib/monitor.py' %(os.getcwd()), )
            monit_job.minute.every(data['monitor_minutes'])

            ping_job = users_cron.new(command='/usr/bin/python3 %s/monitoring/lib/ping.py' %(os.getcwd()), )
            ping_job.minute.every(data['ping_check'])

            backup_job = users_cron.new(command='/usr/bin/python3 %s/monitoring/lib/backup.py' %(os.getcwd()), )
            backup_job.day.every(data['backup_days'])

            users_cron.write()
            return HttpResponseRedirect('/')
    else:
        form = CronForm()

    return render(request, 'monitoring/cron.html', {'form': form})
