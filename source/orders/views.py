from rest_framework import viewsets, views, generics
from rest_framework import permissions

from .permissions import IsAdmin
from .models import Order, OrderItem
from .serializers import  OrderItemSerializer, OrderSerializerAdmin, OrderCreationSerializer, OrderGetSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from products.models import Menu
from shifts.models import Shift


class OrderViewSet(viewsets.ModelViewSet):
    """
    CRUD for Orders
    """
    queryset = Order.objects.all().prefetch_related('order_items')
    permission_classes = [permissions.AllowAny]



    def get_serializer_class(self):

        if self.request.method in ["POST", "PUT", "PATCH"]:
            return OrderCreationSerializer

        else:
            return OrderGetSerializer


    def create(self, request, *args, **kwargs):
        # Getting the current shift to assign it to the order object as its related shift
        request.data["shift"] = Shift.objects.first().id

        return super().create(request, *args, **kwargs)

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
    

    def partial_update(self, request, *args, **kwargs):
        order = self.get_object()
        order_status = request.data.get('order_status', None)
        order_type = request.data.get('order_type', None)
        if order_status:
            order.order_status = order_status
        if order_type:
            order.order_type = order_type
        order.save()
        return Response(
            {
                "message": "Order updated successfully",
                "order": OrderGetSerializer(order).data
            }, 
            status=status.HTTP_200_OK
        )


class OrderItemsViewSet(viewsets.ModelViewSet):
    """
    CRUD for Order Items
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    authentication_classes = (JWTAuthentication,)
    # permission_classes = [, ]
    permission_classes = [permissions.AllowAny, ]


    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)



class OrderViewSetAdmin(viewsets.ModelViewSet):
    http_method_names = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializerAdmin
    permission_classes = [IsAdmin,]
    authentication_classes = (JWTAuthentication,)



class PendingOrderView(viewsets.ModelViewSet):
    # http_method_names = ['get','patch','options','trace']
    queryset = Order.objects.all()
    serializer_class = OrderSerializerAdmin
    # permission_classes = [IsAdmin,]
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (JWTAuthentication,)

    # def get_queryset(self):
    #     queryset = self.queryset
    #     queryset = queryset
    #     return queryset

    def list(self, request, *args, **kwargs):
        print("list")
        last_order = Order.objects.first()
        print(last_order)
        if last_order.order_status == "PENDING":
            return Response({'last_order': OrderSerializerAdmin(last_order).data})
        
        else:
            return Response({'last_order': None})
    

    def partial_update(self, request, *args, **kwargs):
        last_order = self.get_object()
        print(last_order)
        order_status = request.data.get('order_status', None)
        if order_status:
            last_order.order_status = order_status
            last_order.save()
        return Response({
            "message": "Order updated successfully",
            "order": OrderSerializerAdmin(last_order).data
        }, status=status.HTTP_200_OK)
        