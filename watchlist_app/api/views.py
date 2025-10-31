from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def movie_list(request):
    
    if request.method=='GET':
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)  # many=True helps to serialize multiple objects at once
        return Response(serializer.data)  # if only print serializer it will give object info not the data
    
    if request.method=='POST':
        serializer=MovieSerializer(data=request.data)  # request.data contains the data sent by the client

        if serializer.is_valid():
            serializer.save()  # calls create method of serializer
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT','DELETE'])
def movie_detials(request,pk):
    
    if request.method=='GET':
        movie=Movie.objects.get(pk=pk)
        
        serializer=MovieSerializer(movie)  # single object so no need of many=True
        
        return Response(serializer.data)
    
    if request.method=='PUT':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie,data=request.data)  # request.data contains the data sent by the client

        if serializer.is_valid():
            serializer.save()  # calls update method of serializer
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    if request.method=='DELETE':
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response({'message':'Movie deleted successfully!'})