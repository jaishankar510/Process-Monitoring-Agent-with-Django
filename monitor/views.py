
from rest_framework import viewsets, status
from rest_framework.response import Response

from django.shortcuts import render 


from .models import SystemInfo, ProcessInfo
from .serializers import SystemInfoSerializer, ProcessInfoSerializer

class SystemInfoViewSet(viewsets.ModelViewSet):
    queryset = SystemInfo.objects.all().order_by('-created_at')[:1]
    serializer_class = SystemInfoSerializer


class ProcessInfoViewSet(viewsets.ModelViewSet):
    queryset = ProcessInfo.objects.all().order_by('-created_at')[:50]
    serializer_class = ProcessInfoSerializer

    def create(self, request, *args, **kwargs):
        # check if request is a list (bulk insert)
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_bulk_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return super().create(request, *args, **kwargs)

    def perform_bulk_create(self, serializer):
        ProcessInfo.objects.bulk_create([ProcessInfo(**item) for item in serializer.validated_data])




# Frontend


def index(request):
    return render(request, 'index.html')

