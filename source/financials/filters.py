import django_filters
from .models import Cost

class CostFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(choices=Cost.Types.choices)
    user = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
   
    class Meta:
        model = Cost
        fields = {
            'date' : ['gte'],
            'description' : ['icontains'],
            'price' : ['gte'],
            }