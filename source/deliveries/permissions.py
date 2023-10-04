from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrEmployee(BasePermission):
    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS or request.method in ['POST', 'PUT', 'PATCH'] :
        #     return request.user.role == "ADMIN" or request.user.role=="EMPLOYEE"
        # else:
        #      return request.user.role == "ADMIN"

        if request.method in ['DELETE', 'PUT']:
            return request.user.role == "ADMIN"
        
        else:
            return request.user.role == "ADMIN" or request.user.role=="EMPLOYEE"

        
    def has_object_permission(self, request, view, obj):
        # return request.user.role == "ADMIN"
        return request.user.role == "ADMIN" or request.user.role=="EMPLOYEE"