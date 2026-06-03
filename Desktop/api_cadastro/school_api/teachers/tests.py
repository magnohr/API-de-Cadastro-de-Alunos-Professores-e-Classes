from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Teacher

User = get_user_model()

class TeacherAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.url = reverse('teacher-list')
        
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_teacher(self):
        data = {
            'first_name': 'Walter',
            'last_name': 'White',
            'email': 'walter.white@example.com',
            'specialty': 'Chemistry'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Teacher.objects.count(), 1)
        self.assertEqual(Teacher.objects.get().first_name, 'Walter')
