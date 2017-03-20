from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dev_table, name='dev_table'),
    url(r'^config', views.configuration, name='config'),
]