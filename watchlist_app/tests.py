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
        self.token, _ = Token.objects.get_or_create(user=self.user)
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
        
        
        
        
class WatchListTestCase(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='testuser', password='testpassword')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client=APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix", 
                                about="Streaming Platform", website="https://www.netflix.com")
        self.watchlist = models.WatchList.objects.create(Platform=self.stream, title="Example Movie",
                                storyline="Example Movie", active=True)

    def test_watchlist_create(self):
        data = {
            "Platform": self.stream,
            "title": "Example Movie",
            "storyline": "Example Story",
            "active": True
        }
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_watchlist_ind(self):
        response = self.client.get(reverse('movie-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')
        
        
        

class ReviewTestCase(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='testuser', password='testpassword')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client=APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix", 
                                about="Streaming Platform", website="https://www.netflix.com")
        self.watchlist = models.WatchList.objects.create(Platform=self.stream, title="Example Movie",
                                storyline="Example Movie", active=True)
        self.watchlist2 = models.WatchList.objects.create(Platform=self.stream, title="Example Movie",
                                storyline="Example Movie", active=True)
        self.review = models.Review.objects.create(user_review=self.user, rating=8, description="fantastic movie", 
                                watchlist=self.watchlist2, active=True)
    
    def test_review_create(self):
        data = {
            "user_review": self.user,
            "rating": 8,
            "description": "fantastic movie",
            "watchlist": self.watchlist,
            "active": True
        }

        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)

        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauth(self):
        data = {
            "user_review": self.user,
            "rating": 8,
            "description": "fantastic movie",
            "watchlist": self.watchlist,
            "active": True
        }

        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            "user_review": self.user,
            "rating": 4,
            "description": "Great Movie! - Updated",
            "watchlist": self.watchlist,
            "active": False
        }
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_ind(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_ind_delete(self):
        response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_review_user(self):
        url = reverse('user-review-detail')   
        response = self.client.get(url + '?username=' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        

        