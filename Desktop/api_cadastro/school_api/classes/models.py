from django.db import models
from teachers.models import Teacher
from students.models import Student

class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='classes')
    students = models.ManyToManyField(Student, related_name='classes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
