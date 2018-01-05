from django.contrib import admin
from .models import AssignedTo, SensorsLogs, CommandsToDo, PlantProfile

admin.site.register(AssignedTo)
admin.site.register(SensorsLogs)
admin.site.register(CommandsToDo)
admin.site.register(PlantProfile)