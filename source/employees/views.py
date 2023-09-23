from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import Employee
from .serializers import EmployeeSerializer

from .permissions import IsAdmin

class EmployeeViewSetForAdmins(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAdmin, IsAuthenticated,)

    

