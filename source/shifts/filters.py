import django_filters

from .models import Shift


class ShiftFilter(django_filters.FilterSet):
    responsible_employee = django_filters.CharFilter(field_name='responsible_employee__full_name', lookup_expr='icontains')
    class Meta:
        model = Shift
        fields = {
            "start_time": ["gte", 'lte'],
            "end_time": ["gte", 'lte'],
        }


# class ShiftReportFilter(django_filters.FilterSet):
#     related_shift = django_filters.CharFilter(field_name='related_shift__responsible_employee__full_name', lookup_expr='icontains')
#     class Meta:
#         model = ShiftReport
#         fields = {
#             "total_profit": ["gte", 'lte'],
#             "net_profit": ["gte", 'lte'],
#             "total_costs": ["gte", 'lte'],
#         }