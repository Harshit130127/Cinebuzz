from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)  # many=True helps to serialize multiple objects at once
    
    return Response(serializer.data)  # if only print serializer it will give object info not the data


@api_view(['GET'])
def movie_detials(request,pk):
    movie=Movie.objects.get(pk=pk)
    
    serializer=MovieSerializer(movie)  # single object so no need of many=True
    
    return Response(serializer.data)