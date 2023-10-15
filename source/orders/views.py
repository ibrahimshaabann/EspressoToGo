from rest_framework import viewsets
from rest_framework import permissions
from .filters import OrderFilter
from .models import Order, OrderItem
from .serializers import  OrderItemSerializer, OrderSerializerAdmin, OrderCreationSerializer, OrderGetSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from shifts.models import Shift
from attendance.permissions import IsEmployee
from employees.permissions import IsAdmin
from .permissions import IsAdminOrEmployee
from django.core.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend

class OrderViewSet(viewsets.ModelViewSet):
    """
    CRUD for Orders
    """
    queryset = Order.objects.all().prefetch_related('order_items')
    permission_classes = [IsEmployee]
    filterset_class = OrderFilter
    filter_backends = [DjangoFilterBackend, ]


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
    permission_classes = (permissions.AllowAny,)

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



class PendingOrderView(viewsets.ModelViewSet):
    # http_method_names = ['get','patch','options','trace']
    queryset = Order.objects.filter(shift = Shift.objects.first()).prefetch_related('order_items')
    serializer_class = OrderSerializerAdmin
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (JWTAuthentication,)

    def list(self, request, *args, **kwargs):
        last_order = Order.objects.first()
        if last_order.order_status == "PENDING":
            return Response({'last_order': OrderSerializerAdmin(last_order).data})
        
        else:
            return Response({'last_order': None})
    

    def partial_update(self, request, *args, **kwargs):
        last_order = self.get_object()
        order_status = request.data.get('order_status', None)
        if order_status:
            last_order.order_status = order_status
            last_order.save()
        return Response({
            "message": "Order updated successfully",
            "order": OrderSerializerAdmin(last_order).data
        }, status=status.HTTP_200_OK)
        
