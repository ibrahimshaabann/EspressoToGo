import django_filters

from .models import Delivery


class DeliveryFilter(django_filters.FilterSet):
    for_order = django_filters.CharFilter(field_name='for_order__name', lookup_expr='icontains')
    reposnisble_employee = django_filters.CharFilter(field_name='reposnisble_employee__full_name', lookup_expr='icontains')
    class Meta:
        model = Delivery
        fields = {
            "created": ["gte", 'lte'],
            "delivered": ["exact"],
        }