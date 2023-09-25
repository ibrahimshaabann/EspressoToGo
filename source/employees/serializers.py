from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    """
    This serializer class is used when admins try to EXECUTE 'CRUD' Operations on Employees.
    
    The Employee model Itself does not have full_name, username, email, phone_number, gender, and birth_date fields
    Instead it inherits them from the Person model and those fields are not required when creating an instance of the employee.
    
    #######################
    
    Required fields:
    
    "role", "employee", "password", "salary" 
    
    """

    def create(self, validated_data):
        password = validated_data.pop("password")
        employee = Employee(**validated_data)
        employee.set_password(password)
        employee.save()
        return employee
    
    
    class Meta:
        model = Employee
        exclude = ("is_superuser", "is_staff", "groups", "user_permissions",)



class EmployeeSerializerOnShifts(serializers.ModelSerializer):

    """
    This serializer class is used to display Employees data when getting shifts and shifts reports.
    
    """

    class Meta:
        model = Employee
        exclude = (
            "id", "username", "email",
            "is_superuser", "is_staff", "groups", 
            "user_permissions", 'last_login', 
            'birth_date', 'salary', 'password', 'gender', 'role'
        )