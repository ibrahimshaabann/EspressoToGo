from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsEmployeeOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in (SAFE_METHODS, 'POST', 'PUT'):
            return request.user.role == "ADMIN" or request.user.role == "Employee"
        
        else:
            return False 
    

    def has_object_permission(self, request, view, obj):
        return request.user.role == "ADMIN"
