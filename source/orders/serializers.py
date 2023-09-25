from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    # menu_item = serializers.StringRelatedField()
    
    

    class Meta:
        model = OrderItem
        fields = '__all__'
        # exclude = ('order',)


    def create(self, validated_data):
    
        total_price = validated_data['menu_item'].price * validated_data['quantity']
        OrderItem.objects.create(total_price=total_price, **validated_data)
        return super().create(validated_data)

    

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    
