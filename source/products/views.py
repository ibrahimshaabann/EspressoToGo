from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Menu
from .serializers import MenuSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
# Create your views here.
