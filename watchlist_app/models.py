from django.db import models

# Create your models here.


class Movie(models.Model):  # models.Model is used to create a model in django,it is a base class for all models in django
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    active=models.BooleanField(default=True)
    
    
    def __str__(self): # the reason of using it because without it, django will show object1,object2 instead of movie names in admin panel
        return self.name