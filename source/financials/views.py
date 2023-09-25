from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CostFilter
from .models import Cost
from .serializers import CostSerializer

class CostViewSet(ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    # authentication_classes = None
    # permission_classes = None
    filterset_class = CostFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['date', 'description','date', ]