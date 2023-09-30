from rest_framework import serializers
from .models import Shift, ShiftReport
from employees.serializers import EmployeeSerializer, EmployeeSerializerOnShifts


class ShiftEmployeeSerizlier(serializers.ModelSerializer):
    responsible_employee = serializers.StringRelatedField()
    class Meta:
        model = Shift
        fields = '__all__'
        

    def update(self, instance, validated_data):
        """
        Override the update method to recieve only the end_time and don't recieve
        any other data seny by the PUT request
        """
        instance.end_time = validated_data['end_time']
        instance.save()
        return instance
    
    
    # def to_representation(self, instance):
        # representation = super().to_representation(instance)


class ShiftAdminSerizlier(serializers.ModelSerializer):
    """
    Note that we want to show 
    """
    responsible_employee = serializers.StringRelatedField()
    class Meta:
        model = Shift
        fields = '__all__'


# class ShiftReportSerizlier(serializers.ModelSerializer):
#     """
#     Don't forget to include another serializer
#     """

#     related_shift = ShiftEmployeeSerizlier()

#     class Meta:
#         model = ShiftReport
#         fields = '__all__'

    