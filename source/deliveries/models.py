from django.db import models
from models_extensions.models import TimeStampedModel
from customers.models import Customer
from orders.models import Order
from employees.models import Employee
from products.validators import validate_price

class Delivery(TimeStampedModel):
    description = models.TextField(null=True, blank=True,verbose_name="الوصف")
    address = models.TextField(null=True, blank=True,verbose_name="العنوان")
    delivered = models.BooleanField(default=False,verbose_name="تم التوصيل")
    for_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, related_name='order_deliveries',verbose_name="رقم الاوردر")
    responsible_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='employee_deliveries',verbose_name="الموظف المسئول")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False, related_name='customer_delivery',verbose_name="العميل")
    tax = models.DecimalField(null=True, blank=True, verbose_name="tax", default=0.00,max_digits=7, decimal_places=2, validators=[validate_price])
    
    class Meta:
        db_table = 'deliveries'
        verbose_name = 'Delivery'
        verbose_name_plural = 'الدليفري'
        ordering = ['-id']

    def str(self) -> str:
        return f"{self.id}"
    