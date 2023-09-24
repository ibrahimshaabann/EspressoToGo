import django_filters

from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    
    class Meta:
        model = Employee
        fields = {
            "full_name": ["icontains", "exact"],
            "salary": ["gte", 'lte'],
            "username": ["icontains", 'exact',],
            "email": ["icontains", 'exact',],
            "phone_number": ["icontains"],
        }