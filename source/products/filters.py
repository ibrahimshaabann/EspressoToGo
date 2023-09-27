import django_filters
from .models import Menu

class MenuFilter(django_filters.FilterSet):
    # Here we filter menu items according to their category name
    category = django_filters.CharFilter(field_name="category__name",
                                         lookup_expr="iexact")
    
    # description = django_filters.CharFilter(field_name='description', lookup_expr='contains')
    available = django_filters.BooleanFilter(field_name='available')
   
    class Meta:
        model = Menu
        fields = {
            'name' : ['icontains','exact'],
            'price' : ['gte', 'lte'],
            }
        
    
        

 