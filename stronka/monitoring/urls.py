from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.device_list, name='device_list'),
]