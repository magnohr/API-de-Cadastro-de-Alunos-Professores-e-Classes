from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Student
from datetime import date, timedelta

User = get_user_model()

class StudentAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.url = reverse('student-list')
        
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_unauthenticated_request_fails(self):
        self.client.credentials()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_student(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'birth_date': '2010-05-15',
            'registration_number': 'STU001'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().first_name, 'John')

    def test_create_student_future_birth_date(self):
        future_date = date.today() + timedelta(days=1)
        data = {
            'first_name': 'Future',
            'last_name': 'Student',
            'email': 'future@example.com',
            'birth_date': future_date.isoformat(),
            'registration_number': 'STU002'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('birth_date', response.data)
        self.assertEqual(response.data['birth_date'][0], "A data de nascimento não pode ser no futuro.")
