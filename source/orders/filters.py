import django_filters
from .models import Order
class OrderFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')
    
    class Meta:
        model = Order
        fields = '__all__'