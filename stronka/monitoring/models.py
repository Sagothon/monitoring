from django.db import models

class Device(models.Model):
    ip = models.CharField(max_length = 100, null=True)
    login = models.CharField(max_length = 100, null=True)
    password = models.CharField(max_length = 100, null=True)
    port = models.IntegerField(null=True)
    status = models.CharField(max_length = 100, null=True)
    dev_name = models.CharField(max_length = 100, null=True)
    firmware = models.CharField(max_length = 100, null=True)
    wireless_mode = models.CharField(max_length = 100, null=True)
    signal = models.IntegerField(null=True)
    ccq = models.IntegerField(null=True)
    air_q =models.IntegerField(null=True)
    air_c = models.IntegerField(null=True)
    freq = models.IntegerField(null=True)
    uptime = models.IntegerField(null=True)
    product = models.CharField(max_length = 100, null=True)
    last_seen = models.CharField(max_length = 100, null=True)
    ping = models.CharField(max_length = 100, null=True)
    error = models.CharField(max_length = 100, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.ip
