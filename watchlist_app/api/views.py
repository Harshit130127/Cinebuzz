from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class MovieListAV(APIView):
    
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)  # many=True helps to serialize multiple objects at once
        return Response(serializer.data)  # if only print serializer it will give object info not the data
    
    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # calls create method of serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class MovieDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        movie= Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie, data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # calls update method of serializer
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        movie= Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    