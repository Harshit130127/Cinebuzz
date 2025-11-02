from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    # watchlist = serializers.CharField(source='watchlist.title', read_only=True)  # to show the title of the watchlist item instead of its id
    
    user_review = serializers.StringRelatedField(read_only=True)  # to show the username of the user who gave the review
    
    class Meta:
        model = Review
        # fields = "__all__"
        exclude=('watchlist',) # we are excluding watchlist field here because we are showing it using nested serialization in WatchListSerializer


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
        

        
