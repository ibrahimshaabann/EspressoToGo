from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrEmployee(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.method == "POST":
            return request.user.role == "ADMIN" or request.user.role=="EMPLOYEE"
        else:
             return request.user.role == "ADMIN"
    def has_object_permission(self, request, view, obj):
        return request.user.role == "ADMIN"