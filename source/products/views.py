from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from products.filters import MenuFilter
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all().distinct('name').order_by('name')
    serializer_class = MenuSerializer
    # authentication_classes = None
    # permission_classes = None
    filterset_class = MenuFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'name', 'category']
