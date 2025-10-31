from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    ''' Serializer for Movie model and is used to convert complex data such as querysets and 
    model instances to native Python and the fields must be same as in the model'''
    
    len_name=serializers.SerializerMethodField() # custom field to get length of name,this field is not present in the database model
    
    
    class Meta:
        model = Movie
        fields = "__all__"  # to include all fields of the model
        
        # exclude = ['id']  # to exclude specific fields like id
        
        
        
        
    
    def get_len_name(self, object): # this object is the instance of the model
        length= len(object.name)
        return length
        
        
    def validate(self, data):  # object-level validation
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description cannot be the same")
        else:
            return data
        
    
    def validate_name(self, value):  # field-level validation for name field
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        
        return value





'''this is for serializers.Serializer not modelSerializer'''


# def name_length(value):   # custom validator function
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")

# class MovieSerializer(serializers.Serializer):
#     ''' Serializer for Movie model and is used to convert complex data such as querysets and 
#     model instances to native Python and the fields must be same as in the model'''
    
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(max_length=100,validators=[name_length])
#     description=serializers.CharField(max_length=300)
#     active=serializers.BooleanField()
    
    
#     def create(self, validated_data):
#         '''this will unpack the validated_data dictionary and
#         pass it as keyword arguments to create a new Movie instance.'''
        
#         return Movie.objects.create(**validated_data)  # this ** here is used to unpack the dictionary
    
    
#     def update(self, instance, validated_data):
        
#         instance.name = validated_data.get('name', instance.name) # instance here is the previous object
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
        
#         return instance
    
    
#     def validate(self, data):  # object-level validation
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description cannot be the same")
#         else:
#             return data
    
    
    
    
#     # def validate_name(self, value):  # field-level validation for name field
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short")
        
#     #     return value