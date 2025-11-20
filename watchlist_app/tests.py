from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase  # it is used to create test cases
from rest_framework.test import APIClient  # it is used to make requests in tests
from watchlist_app import models

class StreamPlatformTestCase(APITestCase):
    
    
    def setUp(self):
        self.user=User.objects.create_user(username='testuser', password='testpassword')
        self.token=Token.objects.get(user=self.user)
        self.client=APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
        self.stream=models.StreamPlatform.objects.create(
            name='Netflix', website='https://www.netflix.com', about='Streaming Platform')
    
    def test_stream_platform_create(self):
        
        url=reverse('streamplatform-list')  # getting the url for stream platform list/create view
        data={
            'name':'Netflix',
            'about':'Streaming Platform',
            'website':'https://www.netflix.com'
        }
        
        response=self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) # only admin can create stream platform items
        
        
        
    def test_stream_platform_list(self):
        
        response=self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_stream_platform_detail(self):
        
        response=self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)