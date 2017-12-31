from django.db import models
from django.utils import timezone


class AssignedTo(models.Model):
    username = models.CharField(max_length=250)
    actualName = models.CharField(max_length=250, default='john doe')
    linked = models.BooleanField(default=False)

    def __str__(self):
        return self.actualName


class CommandsToDo(models.Model):
    cmd_name = models.CharField(max_length=250, primary_key=True)
    pi_mac = models.CharField(max_length=250)


class SensorsLogs(models.Model):
    pi_mac = models.CharField(max_length=250, default="00:00:00:00:00:00")
    heat = models.CharField(max_length=250)
    light = models.CharField(max_length=250)
    moist = models.CharField(max_length=250)
    rain = models.CharField(max_length=250)
    water_lvl = models.CharField(max_length=250)
    sync_time = models.DateTimeField(auto_now_add=True, primary_key=True)

