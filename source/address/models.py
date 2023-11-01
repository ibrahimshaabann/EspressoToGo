from django.db import models

from customers.models import Customer


class Address(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name="العميل")
    address = models.TextField(verbose_name="العنوان")

    class Meta:
        verbose_name_plural = "العناوين"
        db_table = "address"
    def __str__(self):
        return f"{self.address}"