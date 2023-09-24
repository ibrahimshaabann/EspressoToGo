from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.filters import SearchFilter


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # authentication_classes = None
    # permission_classes = None
    filter_backends = [SearchFilter,]
    search_fields = ['id', 'name', 'category']
