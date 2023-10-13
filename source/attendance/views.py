import json
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.filters import SearchFilter

from employees.models import Employee
from employees.serializers import EmployeeSerializerOnAttendance
from .models import Attendance
from .serializers import AttendanceSerializer
from .filters import AttendanceOutTimeFilterBackend
from rest_framework.permissions import AllowAny
from .permissions import IsEmployee
from employees.permissions import IsAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class AttendanceViewSet(ModelViewSet):
    
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [SearchFilter,AttendanceOutTimeFilterBackend]
    search_fields = ["employee_attended__full_name"]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def create(self, request, *args, **kwargs):
        employee_id = request.data['employee_attended']
        employee = get_object_or_404(Employee, pk=employee_id)
        attendance = Attendance.objects.create(employee_attended = employee, user_created_the_attendance=request.user,)
        attendance.save()
        serializer = AttendanceSerializer(attendance)
        return Response({
            "status": "Created",
            "data": serializer.data
        },
        status = status.HTTP_200_OK
        )
    def update(self, request, *args, **kwargs):
        
        instance = self.get_object()
        out_time = request.data.get('out_time')

        # update() method to update the instance
        Attendance.objects.filter(id=instance.id).update(
            out_time=out_time,
        )

        # Reload the updated instance from the database
        instance.refresh_from_db()

        serializer = AttendanceSerializer(instance)
        return Response({
            "status": "Updated",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

class AllAttendanceViewSet(ModelViewSet):

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [SearchFilter]
    search_fields = ["employee_attended"]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]


    


class EmployeeAttendanceViewSet(ViewSet):

    """
    This view is used to get the employees those whom are not currently in the place   
    """

    authentication_classes = [JWTAuthentication]
    def list(self, request):
        employees = Employee.objects.exclude(
            employee_attendance__out_time__isnull=True
        ).distinct()
        serializer = EmployeeSerializerOnAttendance(employees, many=True)
        return Response(serializer.data)