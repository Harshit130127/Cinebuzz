from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = "__all__"
        
        

class WatchListSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True, read_only=True)  # nested serialization to show reviews related to watchlist item
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    watchlist=WatchListSerializer(many=True, read_only=True)  # nested serialization to show watchlist items related to stream platform
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        

        
