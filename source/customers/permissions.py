from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsAdmin(BasePermission):
    """
    Custom permission to allow only admin users to access. 
    """

    def has_permission(self, request, view):
        if not request.method == "DELETE":
            return request.user.role in ["ADMIN", "EMPLOYEE"]
        
    """
    Object-level permission to only allow only admins to edit.
    """

    def has_object_permission(self, request, view, obj):
        if not request.method == "DELETE":
            return request.user.role in ["EMPLOYEE", "ADMIN"]
    