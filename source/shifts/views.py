from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ShiftSerizlier, ShiftReportSerizlier
from .models import Shift, ShiftReport
from rest_framework.permissions import AllowAny

class ShfitViewSet(ModelViewSet):
    http_method_names = ['get', 'retrieve', 'patch', 'options', 'trace','post']
    queryset = Shift.objects.all()
    serializer_class = ShiftSerizlier
    # authentication_classes = None
    permission_classes = (AllowAny,)
    # filterset_class = None
    filter_backends = [SearchFilter,OrderingFilter, DjangoFilterBackend]
    search_fields = ['id',
                    'responsible_employee__full_name',
                    'responsible_employee__username',
                    'responsible_employee__phone_number']
    ordering_fields = ['start_time',]
    

class ShfitReportViewSet(ModelViewSet):
    http_method_names = ['get', 'retrieve', 'patch', 'options', 'trace','post']
    queryset = ShiftReport.objects.all()
    serializer_class = ShiftReportSerizlier
    # authentication_classes = None
    permission_classes = (AllowAny,)
    # filterset_class = None
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['id',
                    'responsible_employee__full_name',
                    'responsible_employee__username',
                    'responsible_employee__phone_number']
    ordering_fields = ['total_profit',
                       'net_profit',
                       'total_costs']
    

# Create your views here.
