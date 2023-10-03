from rest_framework import serializers
from .models import Customer
from django.contrib.auth.hashers import make_password



class CustomerSerializer(serializers.ModelSerializer):
    
    """
    This serializer class is used when admins try to EXECUTE 'CRUD' Operations on Customers.
    
    and Customers Sign-Up

    The Customer model Itself does not have full_name, username, email, phone_number, gender, and birth_date fields
    Instead it inherits them from the Person model.
    
    """
    
    # Allow null values for password field.
    
    
    def create(self, validated_data):

        """
        Considering the fact that the Admin model inherits from the Person model,
        All person fields are allow null values. even the password.
        But here we can get all fields that are required for creating admins.
        """
        
        validated_data["password"] = make_password(validated_data["password"])

        validated_data["full_name"] = validated_data["full_name"]
        validated_data["phone_number"] = validated_data["phone_number"]

        return super().create(validated_data)
    
    class Meta:
        model = Customer
        exclude = ("is_superuser", "is_staff", "groups", "user_permissions",)
        




class CustomerSerializerForDisplayingCustomerData(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ("is_superuser", "is_staff", "groups", "user_permissions",)
        