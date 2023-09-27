from rest_framework import serializers
from .models import Delivery

from orders.serializers import OrderSerializerForDisplayingDeliveryData

class DeliverySerializer(serializers.ModelSerializer):
    # for_order = serializers.StringRelatedField()
    for_order = OrderSerializerForDisplayingDeliveryData()
    responsible_employee = serializers.StringRelatedField()

    class Meta:
        model = Delivery
        # fields = '__all__'
        exclude = ('modified',)
    