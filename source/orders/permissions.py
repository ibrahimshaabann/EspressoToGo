from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.role == "ADMIN"
        elif request.method == "DELETE" and request.user.role == "ADMIN":
            return True  # Allow DELETE requests made by admins
        return False  # Return False for all other methods
        
    def has_object_permission(self, request, view, obj):
        if request.user.role == "ADMIN" and request.method == "DELETE":
            obj.order_status = "CANCELED"
            # obj.save()  # Save the object with the updated status
            return True  # Allow the DELETE request without deleting the object

        return True  # For all other methods or if the user is not an admin, allow the request
        

