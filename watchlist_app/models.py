from django.db import models

# Create your models here.


class Movie(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    active=models.BooleanField(default=True)
    
    
    def __str__(self): #it is used to return string representation of the object,it is used where we need to display object as string,because the object by default returns memory address
        return self.name