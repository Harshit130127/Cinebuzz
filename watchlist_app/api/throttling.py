from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    
    scope='review-create'  # referring to the rate limit defined in settings.py
    
    
class ReviewListThrottle(UserRateThrottle):
    
    scope='review-list'  # referring to the rate limit defined in settings.py