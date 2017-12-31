from django.contrib import admin
from .models import AssignedTo, SensorsLogs, CommandsToDo

admin.site.register(AssignedTo)
admin.site.register(SensorsLogs)
admin.site.register(CommandsToDo)
