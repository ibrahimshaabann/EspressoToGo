from rest_framework import serializers
from .models import Ajenda


class AjendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ajenda
        fields = '__all__'

