from django.db import models
from models_extensions.models import TimeStampedModel
from customers.models import Customer
from orders.models import Order
from employees.models import Employee


class Delivery(TimeStampedModel):
    description = models.TextField(null=True, blank=True,verbose_name="الوصف")
    address = models.TextField(null=True, blank=True,verbose_name="العنوان")
    delivered = models.BooleanField(default=False,verbose_name="تم التوصيل")
    for_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, related_name='order_deliveries',verbose_name="رقم الاوردر")
    responsible_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='employee_deliveries',verbose_name="الموظف")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False, related_name='customer_delivery',verbose_name="اسم العميل")
    tax = models.PositiveIntegerField(null=True, blank=True,verbose_name="سعر التوصيل")
    
    class Meta:
        db_table = 'deliveries'
        verbose_name = 'Delivery'
        verbose_name_plural = 'الدليفري'
        ordering = ['-id']

    def str(self) -> str:
        return f"{self.id}"