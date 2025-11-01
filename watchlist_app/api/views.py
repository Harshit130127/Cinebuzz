from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class WatchListAV(APIView):
    
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
    
    
    

class StreamPlatformAV(APIView):
    
    def get(self, request):
        stream=StreamPlatform.objects.all()
        
        serializer=StreamPlatformSerializer(stream, many=True,context={'request':request})
        
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer=StreamPlatformSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class StreamPlatformDetailAV(APIView):
        
    def get(self, request, pk):
        try:
            stream=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=StreamPlatformSerializer(stream)
        
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        stream=StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
    def delete(self, request, pk):
        stream=StreamPlatform.objects.get(pk=pk)
        stream.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)