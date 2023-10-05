from django.db import models
from models_extensions.models import TimeStampedModel
from customers.models import Customer
from orders.models import Order
from employees.models import Employee


class Delivery(TimeStampedModel):
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    delivered = models.BooleanField(default=False)
    for_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, related_name='order_deliveries')
    responsible_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='employee_deliveries')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False, related_name='customer_delivery')
    tax = models.PositiveIntegerField(null=True, blank=True, verbose_name="tax")
    
    class Meta:
        db_table = 'deliveries'
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'
        ordering = ['-id']

    def str(self) -> str:
        return f"{self.id}"