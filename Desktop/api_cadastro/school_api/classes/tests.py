from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.db.models import ProtectedError
from teachers.models import Teacher
from students.models import Student
from .models import Class
from datetime import date

User = get_user_model()

class ClassAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.url = reverse('class-list')
        
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.teacher = Teacher.objects.create(
            first_name='Walter',
            last_name='White',
            email='walter.white@example.com',
            specialty='Chemistry'
        )
        self.student = Student.objects.create(
            first_name='Jesse',
            last_name='Pinkman',
            email='jesse@example.com',
            birth_date=date(1995, 9, 24),
            registration_number='STU101'
        )

    def test_create_class(self):
        data = {
            'name': 'Chemistry 101',
            'teacher': self.teacher.id,
            'students': [self.student.id]
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Class.objects.count(), 1)
        
        list_url = reverse('class-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        class_data = response.data['results'][0]
        self.assertEqual(class_data['name'], 'Chemistry 101')
        self.assertEqual(class_data['teacher']['first_name'], 'Walter')
        self.assertEqual(class_data['students'][0]['first_name'], 'Jesse')

    def test_delete_teacher_protected(self):
        class_obj = Class.objects.create(name='Chemistry 101', teacher=self.teacher)
        class_obj.students.add(self.student)

        with self.assertRaises(ProtectedError):
            self.teacher.delete()
