from rest_framework import viewsets
from rest_framework import permissions
from .models import Order, OrderItem
from .serializers import  OrderItemSerializer, OrderSerializerAdmin, OrderCreationSerializer, OrderGetSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from products.models import Menu
from shifts.models import Shift
from attendance.permissions import IsEmployee
from employees.permissions import IsAdmin
from .permissions import IsAdminOrEmployee
from django.core.exceptions import ValidationError

class OrderViewSet(viewsets.ModelViewSet):
    """
    CRUD for Orders
    """
    queryset = Order.objects.all().prefetch_related('order_items')
    permission_classes = [IsEmployee]


    def get_serializer_class(self):

        if self.request.method in ["POST", "PUT", "PATCH"]:
            return OrderCreationSerializer

        else:
            return OrderGetSerializer

    def create(self, request, *args, **kwargs):
        # Getting the current shift to assign it to the order object as its related shift
        try:
            request.data["shift"] = Shift.objects.first().id 
        except Exception as e:
            raise ValidationError(str(e))

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
        

        # Continue with the update
        return super().update(request, *args, **kwargs)
    


class OrderItemsViewSet(viewsets.ModelViewSet):
    """
    CRUD for Order Items
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    authentication_classes = [JWTAuthentication, ]

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    permission_classes = [IsAdminOrEmployee,]


class OrderViewSetAdmin(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerAdmin
    permission_classes = [IsAdmin,]
    authentication_classes = (JWTAuthentication,)