from rest_framework import serializers
from .models import Class
from teachers.serializers import TeacherSerializer
from students.serializers import StudentSerializer

class ClassWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name', 'teacher', 'students', 'created_at']
        read_only_fields = ['id', 'created_at']

class ClassReadSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ['id', 'name', 'teacher', 'students', 'created_at']
        read_only_fields = ['id', 'created_at']
