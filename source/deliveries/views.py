from django.shortcuts import render
from employees.models import Employee
from orders.models import Order
from .serializers import DeliveryForDisplayingSerializer, DeliveryCreationSerializer
from .models import Delivery
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from .filters import DeliveryFilter
from .permissions import IsAdminOrEmployee
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all().select_related('for_order', 'responsible_employee')
    serializer_class = DeliveryForDisplayingSerializer
    permission_classes = (IsAdminOrEmployee,)
    authentication_classes = [JWTAuthentication]
    throttle_classes = (UserRateThrottle, AnonRateThrottle,)
    filterset_class = DeliveryFilter  
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,]
    search_fields = ['description', 'customer__full_name', 'customer__phone_number']

    def get_serializer_class(self):
        if self.request.method in ['POST', 'GET', 'PATCH']:
            return DeliveryCreationSerializer
        else: 
            return DeliveryForDisplayingSerializer

    def create(self, request, *args, **kwargs):
        """
        Overriding Create method to get the request employee and
        assign it to the delivery object
        """
        retrieved_emp = get_object_or_404(Employee, pk = request.user.id) 
        request.data["responsible_employee"] = retrieved_emp.id  
        return super().create(request, *args, **kwargs)

        
    def partial_update(self, request, *args, **kwargs):
        """
        Only pratch request not put is allowed for cashier
        """
        try:
            # Getting the parameter <pk> sent in the url
            # deliver_obj = Delivery.objects.get(id = kwargs['pk'])
            deliver_obj = self.get_object()
        except Delivery.DoesNotExist:
            return Response(
                {"detail": "Delivery object not found"},
                status = status.HTTP_404_NOT_FOUND
            )
        retrieved_address = request.data.get('address', None)
        retrieved_description = request.data.get('description', None)
        retieved_customer = request.data.get('customer', None)
        retrieved_tax = request.data.get('tax', None)

        if retrieved_address:
            deliver_obj.address = retrieved_address
        if retrieved_description:
            deliver_obj.description = retrieved_description
        if retieved_customer:
            deliver_obj.customer = retieved_customer
        if retrieved_tax:
            deliver_obj.tax = retrieved_tax

        deliver_obj.save()

        return Response(
            DeliveryForDisplayingSerializer(deliver_obj).data,
            status = status.HTTP_200_OK
        ) 
    