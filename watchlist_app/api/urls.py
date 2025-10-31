from django.urls import path, include
from watchlist_app.api import Function_based_views
from watchlist_app.api import views




urlpatterns = [
    path('list/',views.WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/',views.WatchListDetailAV.as_view(),name='movie-detail'),
    path('stream/',views.StreamPlatformAV.as_view(),name='stream-platform-list'),
    path('stream/<int:pk>/',views.StreamPlatformDetailAV.as_view(),name='stream-platform-detail'),
]





'''this is for function based views'''
# urlpatterns = [
#     path('list/',Function_based_views.movie_list,name='movie-list'),
#     path('<int:pk>/',Function_based_views.movie_detials,name='movie-detail'),
# ]
