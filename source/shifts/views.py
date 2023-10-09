from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from admins.models import Admin
from .permissions import IsAdmin, IsEmployee
from django.core.exceptions import ValidationError
from .serializers import ShiftEmployeeSerizlier,ShiftAdminSerizlier
from .models import Shift
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from .filters import ShiftFilter
from orders.models import Order
from financials.models import Cost
from django.shortcuts import get_object_or_404
from employees.models import Employee
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from datetime import datetime

import time

# 0.001372436999999893s Zeyad   
# 0.001200585999999948s Ibrahim 

# return 0 if x == y else 1 if x > y else -1


class ShiftEmployeeViewSet(ModelViewSet):
    http_method_names = ['get', 'retrieve', 'patch', 'options', 'trace','post', 'put']
    queryset = Shift.objects.all()
    serializer_class = ShiftEmployeeSerizlier
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsEmployee,]

    def create(self, request, *args, **kwargs):
        try:
            # Getting the last shift object to check ites end time
            last_shift = Shift.objects.first()

            # Here we get the responsible employee object by the request user name and create a shift object with the esponsible employee object
            new_shift = Shift.objects.create(responsible_employee = get_object_or_404(Employee, pk=request.user.id))

            start_time = time.time()
            if last_shift:
                # if the last created shift has no end_time, set its end_time to  the new shift start_time 
                last_shift.end_time = new_shift.start_time if last_shift and not last_shift.end_time else None
                last_shift.save()
            print(time.time() - start_time)

        except Exception as e:
            return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)

        return Response(ShiftEmployeeSerizlier(new_shift).data, status=status.HTTP_201_CREATED)
    

class ShfitAdminViewSet(ModelViewSet):
    http_method_names = ['get', 'retrieve', 'patch', 'options', 'trace','post']
    queryset = Shift.objects.all()
    serializer_class = ShiftAdminSerizlier
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAdmin,)    ###
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
    filterset_class = ShiftFilter
    
    def benefits(self, request, pk=None):
        print("benefits")
        shift = self.get_object()
        benefits = shift.calculate_benefits()
        shift.calc_menu_items_sales()
        return Response({'benefits': benefits}, status=status.HTTP_200_OK)

        

    # Override the list method to include benefits
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        # Calculate benefits for each Shift  and include it in the response
        # for shift_data in data:
        #     shift = Shift.objects.get(id=shift_data['id'])
        #     shift_data['benefits'] = shift.calculate_benefits()

        return Response(data)

    # Override the retrieve method to include benefits
    def retrieve(self, request, *args, **kwargs):
        print("retrieve")
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        # Calculate benefits for the retrieved Shift and include it in the response
        data['benefits'] = instance.calculate_benefits()
        
        # calculate all sales of menu items in a shift
        data['shift_menu_sales'] = instance.calc_menu_items_sales()

        return Response(data) 
    


    