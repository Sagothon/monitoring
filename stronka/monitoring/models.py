from django.db import models

class Device(models.Model):
    ip = models.CharField(max_length = 100, null=True, blank=True)
    login = models.CharField(max_length = 100, null=True, blank=True)
    password = models.CharField(max_length = 100, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length = 100, null=True, blank=True)
    dev_name = models.CharField(max_length = 100, null=True, blank=True)
    firmware = models.CharField(max_length = 100, null=True, blank=True)
    wireless_mode = models.CharField(max_length = 100, null=True, blank=True)
    ssid = models.CharField(max_length = 100, null=True, blank=True)
    signal = models.IntegerField(null=True, blank=True)
    ccq = models.IntegerField(null=True, blank=True)
    air_q =models.IntegerField(null=True, blank=True)
    air_c = models.IntegerField(null=True, blank=True)
    freq = models.IntegerField(null=True, blank=True)
    uptime = models.FloatField(null=True, blank=True)
    product = models.CharField(max_length = 100, null=True, blank=True)
    last_seen = models.CharField(max_length = 100, null=True, blank=True)
    ping = models.CharField(max_length = 100, null=True, blank=True)
    error = models.CharField(max_length = 100, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.ip
