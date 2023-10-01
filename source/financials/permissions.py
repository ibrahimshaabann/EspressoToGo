from rest_framework.permissions import BasePermission

class IsAdminOrEmployee(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.role == "EMPLOYEE" or request.user.role == "ADMIN"
        
        else :
            return request.user.role == "ADMIN"

        

    def has_object_permission(self, request, view, obj):

        return request.user.role == "ADMIN"