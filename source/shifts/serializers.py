from rest_framework.serializers import ModelSerializer
from .models import Shift, ShiftReport

from employees.serializers import EmployeeSerializer, EmployeeSerializerOnShifts



class ShiftSerizlier(ModelSerializer):
    responsible_employee = EmployeeSerializerOnShifts()
    class Meta:
        model = Shift
        fields = '__all__'



class ShiftReportSerizlier(ModelSerializer):
    """
    Don't forget to include another serializer
    """

    class Meta:
        model = ShiftReport
        fields = '__all__'