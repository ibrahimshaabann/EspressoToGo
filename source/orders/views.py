from rest_framework import viewsets
from rest_framework import permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

from django.shortcuts import get_object_or_404

from products.models import Menu
from shifts.models import Shift


class OrderViewSet(viewsets.ModelViewSet):
    """
    CRUD for Orders
    """
    queryset = Order.objects.all().prefetch_related('order_items')
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]


    def update(self, request, *args, **kwargs):
        # Retrieve the Order object
        order = self.get_object()
        
        # GET order_items from request data
        order_items_data = request.data.get('order_items', None)
        

        # Retrieve the Shift instance with the given shift ID (1 in this case)
        shift_id = request.data.get('shift', None)
        
        shift = get_object_or_404(Shift, pk=shift_id)
        
        if shift:
            # Update the Order with the retrieved Shift instance
            order.shift = shift
            order.save()
        

        if order_items_data:
            # Loop through the order items data
            for item_data in order_items_data:
                # Retrieve the Menu instance with the given menu_item ID
                menu_item_id = item_data.get('menu_item', None)
                menu_item = get_object_or_404(Menu, pk=menu_item_id)

                # Check if an order item with the same menu item and order already exists
                existing_order_item = OrderItem.objects.filter(order=order, menu_item=menu_item).first()

                if existing_order_item:
                    # If it exists, update the quantity
                    existing_order_item.quantity += item_data['quantity']
                    existing_order_item.save()
                else:
                    # If it doesn't exist, create a new OrderItem
                    OrderItem.objects.create(order=order, menu_item=menu_item, quantity=item_data['quantity'])
            
        # Continue with the update
        return super().update(request, *args, **kwargs)


class OrderItemsViewSet(viewsets.ModelViewSet):
    """
    CRUD for Order Items
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.AllowAny]