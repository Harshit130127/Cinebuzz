from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.Serializer):
    ''' Serializer for Movie model and is used to convert complex data such as querysets and 
    model instances to native Python and the fields must be same as in the model'''
    
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    description=serializers.CharField(max_length=300)
    active=serializers.BooleanField()
    
    
    def create(self, validated_data):
        '''this will unpack the validated_data dictionary and
        pass it as keyword arguments to create a new Movie instance.'''
        
        return Movie.objects.create(**validated_data)  # this ** here is used to unpack the dictionary