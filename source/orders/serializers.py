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
    

class OrderGetSerializer(serializers.ModelSerializer):
    """
        This serializer is called in the following cases:
            - Getting all orders, method = GET
            - Retrieve order object, mehtod = Retrieve
    """
    order_items = OrderItemsSerializer(many=True, read_only=True)
    shift = serializers.StringRelatedField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreationSerializer(serializers.ModelSerializer):
    """
        This serializer is called by the overrided create method for orders in OrderViewSet
        Also called when method is put or patch
        we don't need to customize anything
    """
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
 

class OrderSerializerForDisplayingDeliveryData(serializers.ModelSerializer):    

    """
    This Serializer is used in DeliverySerializer to display the order data
    """

    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        

class OrderSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
