from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        """
        Note that delete method is not allowed even for admin
        """
        if request.method == 'DELETE':
            return False 
        
        else: # any other methods except delete are allowed for admin
            print(request.user.role)
            return request.user.role == "ADMIN" 
    

    def has_object_permission(self, request, view, obj):
        return request.user.role == "ADMIN"
    


class IsEmployee(BasePermission):
    def has_permission(self, request, view):

        # The employee is allowed to retrieve his shift only, GET IN GENERAL is not allowed
        if request.method in('POST', 'PUT') or view.action == "retrieve":
            return request.user.role == "EMPLOYEE"
        
        
        # elif request.method == 'PUT' and 'end_time' in request.data:
        #     """
        #     In our login, The employee has the permission to change the out_time for his shift only

        #     """
        #     return request.user.role == "EMPLOYEE"
        
        else:
            return False
    

    def has_object_permission(self, request, view, obj):
        """
        Maybe in this method i may addd the object permission only if this shift object
        related to the user 
        Try to check whether the employee can access or update his shift only 
        by getting the shift id, and check if the user id related to the shift recieved in json
        is same as user id in the request
        """
        # Check if the request is attempting to update the 'end_time' field
        if request.method == 'PUT' and 'end_time' in request.data:
            return request.user.role == "EMPLOYEE"
        
        else:
            # Deny the update for other fields or if the user is not an employee
            return False
        

