from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Admin


class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    """
    This serializer class is used when admins try to Sign-Up.
    
    The Admin model Itself does not have full_name, username, email, phone_number, gender, and birth_date fields
    Instead it inherits them from the Person model.
     
    
    """

       

    def create(self, validated_data): 
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
    
    class Meta:
        model = Admin
        exclude = ("is_superuser", "is_staff", "groups", "user_permissions", )