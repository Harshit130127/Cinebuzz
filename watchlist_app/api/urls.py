from django.urls import include, path
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views

router=DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('',views.WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/',views.WatchListDetailAV.as_view(),name='movie-detail'),
    
    path('list2/',views.WatchListGV.as_view(),name='movie-list2'),

    path('', include(router.urls)),

    path('<int:pk>/reviews/create/', views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/',views.ReviewList.as_view(),name='review-list'), # it is to get all reviews for a particular movie
    path('reviews/<int:pk>',views.ReviewDetail.as_view(),name='review-detail'),  # it is to get, update, delete a particular review
    path('user-reviews/', views.UserReview.as_view(), name='user-review-detail'), # it is to get reviews of a particular user based on the username passed as a query parameter

]





