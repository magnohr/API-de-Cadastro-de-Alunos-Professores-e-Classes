from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-created_at')
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['specialty']
    search_fields = ['first_name', 'last_name', 'email', 'specialty']
    ordering_fields = ['first_name', 'last_name', 'created_at']
