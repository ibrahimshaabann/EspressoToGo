from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Attendance
from .serializers import AttendanceSerializer
from .filters import AttendanceOutTimeFilterBackend
from rest_framework.permissions import AllowAny
from .permissions import IsEmployee
from employees.permissions import IsAdmin

class AttendanceViewSet(ModelViewSet):

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [SearchFilter,AttendanceOutTimeFilterBackend]
    search_fields = ["employee_attended"]
    permission_classes = [AllowAny]

    # permission_classes = [IsEmployee]
    # authentication_classes = []

class AllAttendanceViewSet(ModelViewSet):

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [SearchFilter]
    search_fields = ["employee_attended"]
    permission_classes = [AllowAny]

    # permission_classes = [IsAdmin]
    # authentication_classes = []
