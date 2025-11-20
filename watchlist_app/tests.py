from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase  # it is used to create test cases
from rest_framework.test import APIClient  # it is used to make requests in tests


class StreamPlatformTestCase(APITestCase):
    
    def test_stream_platform_create(self):
        
        url=reverse('streamplatform-list')  # getting the url for stream platform list/create view
        data={
            'name':'Netflix',
            'about':'Streaming Platform',
            'website':'https://www.netflix.com'
        }
        
        response=self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)