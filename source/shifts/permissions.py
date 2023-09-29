from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        """
        Note that delete method is not allowed even for admin
        """
        if request.method == 'DELETE':
            return False 
        
        else: # any other methods except delete are allowed for admin
            return request.user.role == "ADMIN" 
    

    def has_object_permission(self, request, view, obj):
        return request.user.role == "ADMIN"
    

class IsEmployee(BasePermission):
    def has_permission(self, request, view):

        # The employee is allowed to retrieve his shift only, GET IN GENERAL is not allowed
        if request.method in('POST','PUT','GET') or view.action == "retrieve":
            return request.user.role == "EMPLOYEE"
        
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

        # This means username of the the employee  making request
        request_username = request.user.username 

        # This is the username of the employee responsible for the shift
        shift_user_username =  obj.responsible_employee.username

        print(request.method)
        # Check if the request is attempting to update the 'end_time' field 
        if request.method == 'PUT' and 'end_time' in request.data or view.action=="retrieve":
            return request.user.role == "EMPLOYEE" and shift_user_username == request_username       
        else:
            # Deny the update for other fields or if the user is not an employee
            return False
        

