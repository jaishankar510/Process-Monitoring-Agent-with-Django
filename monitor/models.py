from django.db import models

class SystemInfo(models.Model):
    hostname = models.CharField(max_length=100)
    os = models.CharField(max_length=50)
    os_version = models.CharField(max_length=100)
    cpu_count = models.IntegerField()
    total_memory = models.FloatField()
    available_memory = models.FloatField()
    disk_usage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class ProcessInfo(models.Model):
    name = models.CharField(max_length=100)
    memory_usage = models.FloatField()
    cpu_usage = models.FloatField()
    ppid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
