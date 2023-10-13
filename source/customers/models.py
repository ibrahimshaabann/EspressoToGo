from django.db import models

from users.models import Person

from .managers import CustomerManager


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

    objects = CustomerManager()    # Custom Manager for the Customer model used only to filter the admins.




class Customer(CustomerBridge):
    """
    This is the Customer model.
    It is used to create an Customer instance.
    """

    address = models.TextField(blank=True, null=True)


    class Meta:
        db_table = "customers"
        verbose_name = "Customer"
        verbose_name_plural = "الزباين"
    


    