# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse



# def movie_list(request):
#     '''the function movie_list takes a request object as a parameter. 
#         It retrieves all movie objects from the database using Movie.objects.all(). 
#         It then creates a dictionary containing a list of movies, where each movie is represented as a dictionary of its fields and their values. 
#         Finally, it returns this data as a JSON response using JsonResponse.'''

#     movies=Movie.objects.all()  
    
#     data={
#         'movies':list(movies.values())
#         }
    
#     return JsonResponse(data) 


# def movie_detials(request,pk): 
    
#     '''the function movie_details takes a request object and a primary key (pk) as parameters. 
#     It retrieves a specific movie object from the database based on the provided primary key. 
#     It then creates a dictionary containing the movie'''

#     movie=Movie.objects.get(id=pk)  
    
#     data={
#         'name':movie.name,  
#         'description':movie.description,
#         'active':movie.active
#     }
    
#     return JsonResponse(data)