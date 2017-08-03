from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .serializers import Ping_historySerializer
from .models import Ping_history
from django.db import connection
from crontab import CronTab
from .models import Device
from django.shortcuts import render
from django_tables2 import RequestConfig
from .tables import DevicesTable
from .forms import ConfigForm
from .forms import CronForm, MailForm
from .lib.discover import ubnt_discovery
from .lib.ping import ping
from .lib.update import update
#from .lib.monitor import monitor
from .lib.db_connector import siema
import sqlite3
import subprocess
import os



@csrf_exempt
def ping_history_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        history = Ping_history.objects.all()
        serializer = Ping_historySerializer(history, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def ping_history_list_device(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        history = Ping_history.objects.all().filter(device=pk)
    except Ping_history.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Ping_historySerializer(history, many=True)
        return JsonResponse(serializer.data, safe=False)

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
