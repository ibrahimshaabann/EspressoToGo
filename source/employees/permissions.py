from rest_framework.permissions import BasePermission



class IsAdmin(BasePermission):
    """
    Custom permission to allow only admin users to access. 
    """

    def has_permission(self, request, view):
        return request.user.role == "ADMIN"


    """
    Object-level permission to only allow only admins to edit.
    """

    def has_object_permission(self, request, view, obj):

        return request.user.role == "ADMIN"
    