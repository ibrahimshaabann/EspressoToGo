import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    """
    This filter class doesnot work in case of averriding list method in  modelview set
    """
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')
    order_status = django_filters.CharFilter(field_name='order_status', lookup_expr='icontains')
    
    class Meta:
        model = Order
        fields = '__all__'