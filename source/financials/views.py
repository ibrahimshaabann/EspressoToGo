from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Cost
from .serializers import CostSerializer

class CostViewSet(ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    # authentication_classes = None
    # permission_classes = None
    filter_backends = [SearchFilter, ]
    search_fields = ['date', 'description']

