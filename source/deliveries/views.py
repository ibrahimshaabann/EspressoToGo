from django.shortcuts import render
from .serializers import DeliverySerializer
from .models import Delivery
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from django_filters.rest_framework import DjangoFilterBackend
from .filters import DeliveryFilter


from .permissions import IsAdminOrEmployee

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all().select_related('for_order', 'reposnisble_employee')
    serializer_class = DeliverySerializer
    # permission_classes = (IsAdminOrEmployee,)
    permission_classes = (AllowAny,)

    throttle_classes = (UserRateThrottle, AnonRateThrottle,)

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]
    
    filterset_class = DeliveryFilter    
