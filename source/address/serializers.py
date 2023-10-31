from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    # customer = serializers.StringRelatedField()
    class Meta:
        model = Address
        fields = "__all__"
        # exclude = []"id"]