from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """
    For CRUD
    """

    class Meta:
        model = OrderItem
        fields = '__all__'



class OrderItemsSerializer(serializers.ModelSerializer):
    """
    For Order Serializer
    """
    
    menu_item = serializers.StringRelatedField()

    class Meta:
        model = OrderItem
        exclude = ('order',)

    

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemsSerializer(many=True, read_only=True)

    shift = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = '__all__'

    
