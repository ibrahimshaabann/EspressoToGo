from rest_framework.serializers import ModelSerializer

from .models import Cost


class CostSerializer(ModelSerializer):

    class Meta:
        model = Cost
        fields = '__all__'

    
    