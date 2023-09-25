from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all().distinct('name').order_by('name')
    serializer_class = MenuSerializer
    # authentication_classes = None
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter,]
    search_fields = ['id', 'name', 'category']
