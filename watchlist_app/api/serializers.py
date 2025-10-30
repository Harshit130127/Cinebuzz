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
        ''' Create and return a new `Movie` instance, given the validated data.'''
        return Movie.objects.create(**validated_data)