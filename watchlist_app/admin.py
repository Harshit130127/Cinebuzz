from django.contrib import admin
from . import models 
# Register your models here.

admin.site.register(models.Movie)  # registering the Movie model so that it can be managed via the Django admin interface