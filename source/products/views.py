from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.filters import MenuFilter
from .models import Category, Menu
from .serializers import CategorySerializer, MenuSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrEmployee

class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all().distinct('name').order_by('name')
    serializer_class = MenuSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAdminOrEmployee,]
    filterset_class = MenuFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'name', 'category']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAdminOrEmployee, ]
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    search_fields = ['name']
