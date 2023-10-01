from decimal import Decimal
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CostFilter
from .models import Cost
from orders.models import Order
from .serializers import CostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from employees.permissions import IsAdmin
from employees.models import Employee
from django.shortcuts import get_object_or_404
from shifts.models import Shift
from .permissions import IsAdminOrEmployee


class CostViewSet(ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAdminOrEmployee, ]
    filterset_class = CostFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['date', 'description','date', 'user__username' ]


    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        request.data["user"] = get_object_or_404(Employee, pk=user_id)
        request.data["related_shift"] =  Shift.objects.first().id
        return super().create(request, *args, **kwargs)



class BenefitsViewSet(APIView):

    permission_classes = [IsAdmin,]
    def post(self,request):
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        total_orders_prices = Decimal(0)
        total_costs = Decimal(0)    
        orders_in_duration = Order.objects.filter(
            created_at__gte=start_time,
            created_at__lte=end_time
        )
        for order in orders_in_duration:
            total_orders_prices += order.total_price_of_order

        costs_in_duration = Cost.objects.filter(
            related_shift__start_time__gte=start_time,
            related_shift__end_time__lte=end_time
        )
        for cost in costs_in_duration:
            total_costs += cost.price
        net_profit = total_orders_prices - total_costs
        
        return Response({
            "total_prices": total_orders_prices,
            "total_costs" : total_costs,
            "net_profit": net_profit

        },
        status=status.HTTP_200_OK
        
        )