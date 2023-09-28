from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ShiftSerizlier, ShiftReportSerizlier
from .models import Shift, ShiftReport
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from .filters import ShiftFilter, ShiftReportFilter

from django.shortcuts import get_object_or_404
from employees.models import Employee
from rest_framework.response import Response
from rest_framework import status


class ShfitViewSet(ModelViewSet):
    http_method_names = ['get', 'retrieve', 'patch', 'options', 'trace','post']
    queryset = Shift.objects.all()
    serializer_class = ShiftSerizlier
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)   ###
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = [
        'id',
        'responsible_employee__full_name',
        'responsible_employee__username',
        'responsible_employee__phone_number'
    ]
    ordering_fields = ['start_time',]

    filterset_class = ShiftFilter


    def create(self, request, *args, **kwargs):
        responsible_employee_id = request.data.get('responsible_employee')
        responsible_employee = get_object_or_404(Employee, id=responsible_employee_id)        
        shift = Shift.objects.create(responsible_employee=responsible_employee,)
        shift.save()
        return Response(ShiftSerizlier(shift).data, status=status.HTTP_201_CREATED)
        


class ShfitReportViewSet(ModelViewSet):
    http_method_names = ['get', 'retrieve', 'patch', 'options', 'trace','post']
    queryset = ShiftReport.objects.all()
    serializer_class = ShiftReportSerizlier
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)    ###
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = [
        'id',
        'responsible_employee__full_name',
        'responsible_employee__username',
        'responsible_employee__phone_number'
    ]
    ordering_fields = [
        'total_profit',
        'net_profit',
        'total_costs',
    ]
    filterset_class = ShiftReportFilter
    