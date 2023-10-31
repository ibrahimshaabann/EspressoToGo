from django.db import models

from customers.models import Customer


class Address(models.Model):
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField(default=False)
