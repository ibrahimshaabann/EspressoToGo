from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsAdmin(BasePermission):
    """
    Custom permission to allow only admin users to access. 
    """

    def has_permission(self, request, view):
        if request in SAFE_METHODS or request.user.role == "ADMIN":
            return True
        else:
            return False

    """
    Object-level permission to only allow only admins to edit.
    """

    def has_object_permission(self, request, view, obj):

        return request.user.role == "ADMIN"
    