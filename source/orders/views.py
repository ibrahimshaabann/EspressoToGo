from rest_framework import viewsets
from rest_framework import permissions
from address.models import Address
from .filters import OrderFilter
from .models import Order, OrderItem
from .serializers import  OrderItemSerializer, OrderSerializerAdmin, OrderCreationSerializer, OrderGetSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from customers.models import Customer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from django.shortcuts import get_object_or_404
from shifts.models import Shift
from attendance.permissions import IsEmployee
from employees.permissions import IsAdmin
from .permissions import IsAdminOrEmployee
from django.core.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

class OrderViewSet(viewsets.ModelViewSet):
    """
    CRUD for Orders
    """

    queryset = Order.objects.all().prefetch_related('order_items')
    permission_classes = [IsEmployee]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = OrderFilter

    def get_serializer_class(self):

        if self.request.method in ["POST", "PUT", "PATCH"]:
            return OrderCreationSerializer

        else:
            return OrderGetSerializer
        
    def list(self, request, *args, **kwargs):
        """
        Overriding list method to get s=the current shif tobjects only
        """
        # order_id = self.request.query_params.get('id', None)
        # print("*"*20)
        # print(order_id)

        # self.queryset = self.get_queryset().filter(id=order_id) if order_id else self.get_queryset()
        # print(self.queryset)

        current_shift_orders_queryset = Order.objects.filter(shift = Shift.objects.first()).prefetch_related('order_items')
        order_id = self.request.query_params.get('id', None)
        current_shift_orders_queryset = current_shift_orders_queryset.filter(id=order_id) if order_id else current_shift_orders_queryset
        shift_orders_serializer = self.get_serializer(current_shift_orders_queryset, many=True)
        return Response(shift_orders_serializer.data, status=status.HTTP_200_OK)
   
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
        customer_id = request.data.get('customer', None)
        address_id = request.data.get('address', None)
        address = None
        try:
            customer = Customer.objects.filter(id=customer_id).first()
            if address_id:
                address = Address.objects.get(id=address_id)
        except Exception as e:
            raise ValidationError(str(e))
        
        if order_status:
            order.order_status = order_status
        if order_type:
            order.order_type = order_type
        if customer:
            order.customer = customer
        if address:
            order.address = address
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


class LastOrderView(viewsets.ModelViewSet):
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
    


class PendingOrdersView(viewsets.ModelViewSet):
    queryset = Order.objects.filter(order_status="PENDING").prefetch_related('order_items')
    permission_classes = [IsEmployee, ]
    authentication_classes = [JWTAuthentication, ]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = OrderFilter
    
    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'PUT']:
            return OrderCreationSerializer
        
        elif self.request.method == 'GET':
            return OrderGetSerializer
        
    def list(self, request, *args, **kwargs):
        order_id = self.request.query_params.get('id', None)

        try:
            # if id queryparam is sent in the url, filter the returned result. else, retrieve all pending orders
            self.queryset = self.get_queryset().filter(id=order_id) if order_id else self.get_queryset()
        except Exception as e:
            print(str(e))

        serializer = self.get_serializer(self.queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        # order_id = self.kwargs.get('pk')
        order_instance = self.get_object()
        retreived_order_status = request.data['order_status']
        order_instance.order_status = retreived_order_status if retreived_order_status else order_instance.order_status
        order_instance.save()
        order_serializer = self.get_serializer(order_instance)
        return Response(order_serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        order_instance = self.get_object()
        order_serializer = self.get_serializer(order_instance)
        return Response(order_serializer.data, status=status.HTTP_200_OK)
    

    

