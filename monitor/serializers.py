
from rest_framework import serializers
from .models import SystemInfo, ProcessInfo

class SystemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemInfo
        fields = '__all__'

class ProcessInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessInfo
        fields = '__all__'
