from rest_framework import viewsets
from .models import Class
from .serializers import ClassReadSerializer, ClassWriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all().order_by('-created_at')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['teacher']
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ClassReadSerializer
        return ClassWriteSerializer
