from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Employee



class CashierSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, allow_null=True, write_only=True)

    """
    This serializer class is used when to create Cashiers' Account using only thire full_name.
    """
    

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['full_name'] = validated_data['full_name'].lower()
        return super().create(validated_data)
    
    class Meta:
        model = Employee
        exclude = ("is_superuser", "is_staff", "groups", "user_permissions", 'last_login', 'gender')



class EmployeeSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    """
    If we need to create a cashier without a passowrd we can use this serializer. with commented password field.
    And we can Extended our serializer to have a password field.
    and create employees with passwords. and all other person fields
    """
    
    """
    This serializer class is used when admins try to EXECUTE 'CRUD' Operations on Employees.
    
    The Employee model Itself does not have full_name, username, email, phone_number, gender, and birth_date fields
    Instead it inherits them from the Person model.
    
    """

    def create(self, validated_data):
        # validated_data['username'] = validated_data['username'].lower()
        # validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
    
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
        # exclude = ("is_superuser", "is_staff", "groups", "user_permissions",)



class EmployeeSerializerOnAttendance(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("full_name",)
