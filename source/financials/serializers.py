from rest_framework import serializers

from .models import Cost


class CostSerializer(serializers.ModelSerializer):
    # changing the datetime field format
    date = serializers.DateTimeField(format='%d/%m/%Y %H:%M', required=False)
    class Meta:
        model = Cost
        fields = '__all__'
        # exclude = ('date',)

    
    