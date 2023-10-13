from rest_framework import serializers
from .models import Delivery

from orders.serializers import OrderSerializerForDisplayingDeliveryData

class DeliveryForDisplayingSerializer(serializers.ModelSerializer):
    for_order = OrderSerializerForDisplayingDeliveryData()
    responsible_employee = serializers.StringRelatedField()
    created = serializers.DateTimeField(format='%d/%m/%Y %H:%M', required=False)

    class Meta:
        model = Delivery
        exclude = ('modified',)
    
class DeliveryCreationSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d/%m/%Y %H:%M', required=False)
    
    class Meta:
        model = Delivery
        exclude = ('modified',)