from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient  # it is used to make requests in tests

class RegisterTestCase(APITestCase):
    
    # for these we are not using database,the django test framework will create a test database for us
    
    
    def test_register_user(self):   # it must start with test_ 
        url = reverse('register')  # it takes the name of the url pattern and returns the actual url
        data = {
            'username': 'testuser',
            'email':'testuser@example.com',
            'password': 'testfordrf',
            'password2': 'testfordrf'
            }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # comparing expected status code with actual status code