from rest_framework import serializers
from .models import Shift, ShiftReport

from employees.serializers import EmployeeSerializer, EmployeeSerializerOnShifts


class ShiftSerizlier(serializers.ModelSerializer):
    responsible_employee = EmployeeSerializerOnShifts()
    class Meta:
        model = Shift
        fields = '__all__'



class ShiftReportSerizlier(serializers.ModelSerializer):
    """
    Don't forget to include another serializer
    """

    related_shift = ShiftSerizlier()

    net_profit = serializers.DecimalField(
        decimal_places=2,
        max_digits=10,
        read_only=True
    )

    class Meta:
        model = ShiftReport
        fields = '__all__'