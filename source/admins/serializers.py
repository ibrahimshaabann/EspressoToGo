from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Admin



class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    """
    This serializer class is used when admins try to Sign-Up.
    'In our base User Class password is not required, but in the Admin model we serialize it as required'
    The Admin model Itself does not have full_name, username, email, phone_number, gender, and birth_date fields
    Instead it inherits them from the Person model.
     
    """

    
    def create(self, validated_data): 

        """
        Considering the fact that the Admin model inherits from the Person model,
        All person fields are allow null values.
        But here we can get all fields that are required for creating admins.
        """

        validated_data["password"] = make_password(validated_data["password"])
        validated_data["username"] = validated_data["username"].lower()
        return super().create(validated_data)
    
    class Meta:
        model = Admin
        exclude = ("is_superuser", "is_staff", "groups", "user_permissions", )