import django_filters

from .models import Delivery


class DeliveryFilter(django_filters.FilterSet):
    class Meta:
        model = Delivery
        fields = {
            "for_order__name": ["icontains"],
            "reposnisble_employee": ["exact"],
            "created": ["gte", 'lte'],
            "delivered": ["exact"],
        }