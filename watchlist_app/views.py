from django.shortcuts import render
from .models import Movie

from django.http import JsonResponse
# Create your views here.



def movie_list(request):
    movies=Movie.objects.all()  # it is used to fetch all the movie objects from the database in the form of a queryset or list
    data={
        'movies':list(movies.values())
        }
    return JsonResponse(data)  # values() method is used to convert the queryset into a list of dictionaries where each dictionary represents a movie object with its fields and their values