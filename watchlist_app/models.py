from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from django.contrib.auth.models import User



class StreamPlatform(models.Model): # it specifies the streaming platform like netflix,amazon prime etc
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)
    
    def __str__(self):
        return self.name





class WatchList(models.Model):  # models.Model is used to create a model in django,it is a base class for all models in django
    
    Platform=models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist',default=1) # ForeignKey is used to create a many-to-one relationship, here one stream platform can have multiple watchlist items
    
    title=models.CharField(max_length=100)
    storyline=models.CharField(max_length=300)
    active=models.BooleanField(default=True)
    avg_rating=models.FloatField(default=0)  # average rating of the movie
    number_of_ratings=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self): # the reason of using it because without it, django will show object1,object2 instead of movie names in admin panel
        return self.title
    
    
    
class Review(models.Model):
    
    user_review=models.ForeignKey(User, on_delete=models.CASCADE)  # one user can give multiple reviews
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)]) # validators can be used to set min and max value for rating
    description=models.CharField(max_length=200,null=True)
    watchlist=models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews') # one watchlist item can have multiple reviews
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Rating: {self.rating} for {self.watchlist.title}"
