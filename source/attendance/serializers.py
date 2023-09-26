from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ['id','employee_attended', 'in_time', 'out_time', 'user_created_the_attendance',]
