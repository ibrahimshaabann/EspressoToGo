from rest_framework import serializers
from .models import Attendance

from employees.serializers import EmployeeSerializerOnAttendance

class AttendanceSerializer(serializers.ModelSerializer):

    user_created_the_attendance = serializers.StringRelatedField()
    employee_attended = EmployeeSerializerOnAttendance()
    class Meta:
        model = Attendance
        fields = ['id','employee_attended', 'in_time', 'out_time', 'user_created_the_attendance',]