from django.db import models

from users.models import Person

# from .managers import CustomerManager

import uuid

class CustomerBridge(Person):
    """
    This is a proxy model for the Person model.
    It is used to create a separate table for the Customer model.
    This table will not be created on the postgres database tables.
    Instead, it will be used on the admins table as a 'bridge - connector - pointer' to the person model.
    """
    base_role = Person.Role.CUSTOMER

    class Meta:
        proxy = True

    # objects = CustomerManager()    # Custom Manager for the Customer model used only to filter the admins.




class Customer(CustomerBridge):
    """
    This is the Customer model.
    It is used to create an Customer instance.
    """
    # Customer_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    # address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)

    
    def __str__(self):
        return self.username


    class Meta:
        db_table = "customers"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    


    