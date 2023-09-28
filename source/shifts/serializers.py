from rest_framework import serializers
from .models import Shift, ShiftReport
from employees.serializers import EmployeeSerializer, EmployeeSerializerOnShifts



class ShiftEmployeeSerizlier(serializers.ModelSerializer):
    responsible_employee = EmployeeSerializerOnShifts()
    class Meta:
        model = Shift
        fields = '__all__'


class ShiftAdminSerizlier(serializers.ModelSerializer):
    """
    Note that we want to show 
    """
    responsible_employee = serializers.StringRelatedField()
    class Meta:
        model = Shift
        fields = '__all__'



class ShiftReportSerizlier(serializers.ModelSerializer):
    """
    Don't forget to include another serializer
    """

    class Meta:
        model = ShiftReport
        fields = '__all__'