from rest_framework import serializers
from .models import Delivery



class DeliverySerializer(serializers.ModelSerializer):
    for_order = serializers.StringRelatedField()
    responsible_employee = serializers.StringRelatedField()

    class Meta:
        model = Delivery
        # fields = '__all__'
        exclude = ('modified',)
    