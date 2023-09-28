from django.db import models

from models_extensions.models import TimeStampedModel

from orders.models import Order
from employees.models import Employee



class Delivery(TimeStampedModel):
    name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    delivered = models.BooleanField(default=False)
    for_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='order_deliveries')
    reposnisble_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='employee_deliveries')

    