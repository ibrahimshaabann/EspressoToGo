# import django_filters

# from .models import Delivery


# class DeliveryFilter(django_filters.FilterSet):
#     for_order = django_filters.CharFilter(field_name='for_order__id', lookup_expr='icontains')
#     repsosnisble_employee = django_filters.CharFilter(field_name='responsible_employee__full_name', lookup_expr='icontains')
#     customer_phoneNo = django_filters.CharFilter(field_name = 'customer__phone_number', lookup_expr='contains')
#     description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
#     class Meta:
#         model = Delivery
#         fields = {
#             "created": ["gte", 'lte'],
#             "delivered": ["exact"],
#         }