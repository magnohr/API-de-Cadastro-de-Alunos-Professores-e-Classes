from rest_framework import serializers
from .models import Student
from datetime import date

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'birth_date', 'registration_number', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_birth_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("A data de nascimento não pode ser no futuro.")
        return value
