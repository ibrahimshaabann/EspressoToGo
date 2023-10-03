from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "ADMIN" 
    
    def has_object_permission(self, request, view, obj):
        return request.user.role == "ADMIN"
    

 