from .models import Address
import django_filters


class AddressSearchFilter(django_filters.FilterSet):
    
    address = django_filters.CharFilter(field_name='address', lookup_expr='icontains')
    customer = django_filters.CharFilter(field_name='customer')
    
    class Meta:
        model = Address
        fields = "__all__"
    # class Meta:
