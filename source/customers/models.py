from django.db import models
from .validators import valid_phone_number

# from users.models import Person

# from .managers import CustomerManager

# import uuid

# class CustomerBridge(Person):
#     """
#     This is a proxy model for the Person model.
#     It is used to create a separate table for the Customer model.
#     This table will not be created on the postgres database tables.
#     Instead, it will be used on the admins table as a 'bridge - connector - pointer' to the person model.
#     """
#     base_role = Person.Role.CUSTOMER

#     class Meta:
#         proxy = True

#     # objects = CustomerManager()    # Custom Manager for the Customer model used only to filter the admins.




# class Customer(CustomerBridge):
#     """
#     This is the Customer model.
#     It is used to create an Customer instance.
#     """
#     # Customer_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

#     # address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)

#  

class Customer(models.Model):
    full_name = models.CharField(max_length=50,null=False, blank=False,verbose_name='الاسم ',)
    
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    
    first_address = models.TextField(verbose_name='العنوان الاول',null =True,blank =True)
    
    second_address = models.TextField(verbose_name='العنوان الثاني',null =True,blank =True)
    phone_number = models.CharField(
        max_length=20, blank=False, 
        null=True, unique=True, db_index=True,
        validators=[valid_phone_number]
    )    
    
    class Meta:
        db_table = "customers"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self) -> str:
        return f"{self.full_name}"
    
    