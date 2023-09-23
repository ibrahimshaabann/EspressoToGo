import django_filters
from .models import Menu

class MenuFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=Menu.Categories.choices)
    # description = django_filters.CharFilter(field_name='description', lookup_expr='contains')
    available =django_filters.BooleanFilter(field_name='available')
   
    class Meta:
        model = Menu
        fields = {
            'name' : ['icontains','exact'],
            'price' : ['gte', 'lte'],
            }
        

 