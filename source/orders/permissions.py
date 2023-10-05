from rest_framework.permissions import BasePermission

class IsAdminOrEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ["ADMIN", "EMPLOYEE"]
    
    def has_object_permission(self, request, view, obj):
        return request.user.role in ["ADMIN", "EMPLOYEE"]