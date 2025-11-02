from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):  # this base permission class helps to create custom permissions
    
    def has_permission(self, request, view): # has_permission method checks if the user has permission to access the view
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)
    
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_review == request.user or request.user.is_staff
