from django.contrib import admin

# Register your models here.
from monitor.models import SystemInfo,  ProcessInfo

admin.site.register(SystemInfo),
admin.site.register(ProcessInfo),