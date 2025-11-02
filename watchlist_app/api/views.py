from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import serializers


"""For WatchList views"""

class WatchListAV(APIView):
    serializer_class =  WatchListSerializer # it gives the form-like structure of data
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)  # many=True helps to serialize multiple objects at once
        return Response(serializer.data)  # if only print serializer it will give object info not the data
    
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # calls create method of serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class WatchListDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        movie= WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie, data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # calls update method of serializer
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        movie= WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



"""For StreamPlatform views using viewsets"""

class StreamPlatformVS(viewsets.ViewSet):
    
    def list(self,request):
        # queryset=StreamPlatform.objects.all() # here there is an error because the name of the class is same as model name
        queryset=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(queryset, many=True,context={'request':self.request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):  # the function name is predefined in viewsets
        queryset=StreamPlatform.objects.all()
        platform=get_object_or_404(queryset, pk=pk)
        serializer=StreamPlatformSerializer(platform, context={'request':request})
        return Response(serializer.data)
    
    
    def create(self, request):
        serializer=StreamPlatformSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def update(self, request, pk=None):
        platform = get_object_or_404(StreamPlatform, pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data,partial=True)
        
        if serializer.is_valid():
            serializer.save()  # updates the existing object
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    
    def destroy(self, request, pk=None):
        platform=StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



"""Concrete Review views using generics"""

class ReviewCreate(generics.CreateAPIView):
    
    serializer_class = ReviewSerializer
    
    
    def get_queryset(self):
        return Review.objects.all()
    
    
    """overwrite query set here because we are not fetching all reviews but creating review for a particular watchlist item"""
    def perform_create(self, serializer):  # it is predefined method in CreateAPIView to customize save behavior
        pk=self.kwargs.get('pk')
        watchlist=WatchList.objects.get(pk=pk)
        
        user_review=self.request.user  # fetching the user who is making the review
        review_queryset=Review.objects.filter(watchlist=watchlist, user_review=user_review) # checking if the user has already reviewed this watchlist item
        
        
        if review_queryset.exists():
            raise serializers.ValidationError("You have already reviewed this watchlist item!")
        
        serializer.save(watchlist=watchlist, user_review=user_review) # saving the watchlist item to which review is being made


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()  # by default it will fetch all the reviews irrespective of watchlist item
    serializer_class = ReviewSerializer   # it gives the form-like structure of data
    
    
    def get_queryset(self):
        pk=self.kwargs['pk']  # fetching pk from url
        Review_list=Review.objects.filter(watchlist=pk)  # filtering reviews based on watchlist item
        return Review_list
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    








"""FOr StreamPlatform views using APIView"""
# class StreamPlatformAV(APIView):
    
#     def get(self, request):
#         stream=StreamPlatform.objects.all()
        
#         serializer=StreamPlatformSerializer(stream, many=True,context={'request':request})
        
#         return Response(serializer.data)
    
    
#     def post(self, request):
#         serializer=StreamPlatformSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# class StreamPlatformDetailAV(APIView):
        
#     def get(self, request, pk):
#         try:
#             stream=StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer=StreamPlatformSerializer(stream)
        
#         return Response(serializer.data)
    
    
#     def put(self, request, pk):
#         stream=StreamPlatform.objects.get(pk=pk)
#         serializer=StreamPlatformSerializer(stream, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
#     def delete(self, request, pk):
#         stream=StreamPlatform.objects.get(pk=pk)
#         stream.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    



"""For Review views using mixins and generics"""

# class ReviewList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer   # it gives the form-like structure of data
    
    
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
    
# class ReviewDetail(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)