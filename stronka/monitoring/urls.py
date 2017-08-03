from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dev_table, name='dev_table'),
    url(r'^config', views.configuration, name='config'),
    url(r'cron', views.cron, name='cron'),
    url(r'^ping_history_list/$', views.ping_history_list),
    url(r'^ping_history_list/(?P<pk>[0-9]+)/$', views.ping_history_list_device),
]