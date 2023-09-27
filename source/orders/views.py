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
        print(shift_id)
        shift = get_object_or_404(Shift, pk=shift_id)
        print(shift)
        if shift:
            # Update the Order with the retrieved Shift instance
            order.shift = shift
            order.save()
        

        if order_items_data:
            # Retrieve the Menu instance with the given menu_item ID (1 in this case)
            menu_item_id = order_items_data.get('menu_item', None)
            menu_item = get_object_or_404(Menu, pk=menu_item_id)
            
            # Create the OrderItem with the retrieved Menu instance
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=order_items_data['quantity'])
            
        # Continue with the update
        return super().update(request, *args, **kwargs)


class OrderItemsViewSet(viewsets.ModelViewSet):
    """
    CRUD for Order Items
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.AllowAny]