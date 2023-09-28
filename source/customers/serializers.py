from rest_framework import serializers
from .models import Customer
from django.contrib.auth.hashers import make_password



class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    """
    This serializer class is used when admins try to EXECUTE 'CRUD' Operations on Customers.
    
    and Customers Sign-Up

    The Customer model Itself does not have full_name, username, email, phone_number, gender, and birth_date fields
    Instead it inherits them from the Person model.
    
    """
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"] )
        return super().create(validated_data)
    
    class Meta:
        model = Customer
        exclude = ("is_superuser", "is_staff", "groups", "user_permissions",)
        


class CustomerSerializerForDisplayingCustomerData(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ("is_superuser", "is_staff", "groups", "user_permissions",)
        