from rest_framework import viewsets, filters

from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Employee
from .serializers import EmployeeSerializer

from .permissions import IsAdmin

from django_filters.rest_framework import DjangoFilterBackend

from .filters import EmployeeFilter


class EmployeeViewSetForAdmins(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAdmin, IsAuthenticated,)
    permission_classes = (AllowAny,)
    
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]
    
    filterset_class = EmployeeFilter


