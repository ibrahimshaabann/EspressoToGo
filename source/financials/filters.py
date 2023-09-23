import django_filters
from .models import Cost

class CostFilter(django_filters.FilterSet):
    cost_type_queryparameter = django_filters.ChoiceFilter(choices=Cost.Types.choices)

    class Meta:
        model = Cost
        fields = ['cost_type_queryparameter']