from django.shortcuts import render
from rest_framework import filters
from .models import Address
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet
from attendance.permissions import IsEmployee
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AddressSerializer
from .filters import AddressSearchFilter

class AddressViewSet(ModelViewSet):

    serializer_class = AddressSerializer
    queryset = Address.objects.all().prefetch_related("customer")
    permission_classes = [IsEmployee]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AddressSearchFilter
