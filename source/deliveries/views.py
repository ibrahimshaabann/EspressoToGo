import json
from django.shortcuts import render

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

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all().select_related('for_order', 'responsible_employee')
    serializer_class = DeliveryForDisplayingSerializer
    permission_classes = (IsAdminOrEmployee,)
    authentication_classes = [JWTAuthentication]
    throttle_classes = (UserRateThrottle, AnonRateThrottle,)
    filterset_class = DeliveryFilter  
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]
    search_fields = ['description', 'customer__full_name', 'customer__phone_number']
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'GET', 'PATCH']:
            return DeliveryCreationSerializer
        else: 
            return DeliveryForDisplayingSerializer

    