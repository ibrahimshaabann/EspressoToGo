import django_filters

from .models import Customer


class CustomerFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(field_name='full_name', lookup_expr='icontains')
    
    class Meta:
        model = Customer
        fields = {
            # "email": ["exact", 'icontains'],
            # "phone_number": ["exact", 'icontains'],
            "username": ["exact", 'icontains'],
        }