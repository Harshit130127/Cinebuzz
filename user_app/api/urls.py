from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views


# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )




urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.registeration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
]
