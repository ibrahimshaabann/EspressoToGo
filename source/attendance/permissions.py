from rest_framework.permissions import BasePermission


class IsEmployee(BasePermission):
    """

    Custom permissions to allow the user to do all methods except DELETE method
    
    """
    def has_permission(self, request, view):
        
        if request.method == 'DELETE':
            return request.user.role == "ADMIN"
    


    def has_object_permission(self, request, view, obj):
                
        if request.method == 'DELETE':
            return request.user.role == "ADMIN"
    
 