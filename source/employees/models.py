from django.db import models

from users.models import Person

from .managers import EmployeeManager

import uuid

from .validators import valid_salary


class EmployeeBridge(Person):

    """
    This is a proxy model for the Person model.
    It is used to create a separate table for the Employee model.
    This table will not be created on the postgres database tables.
    Instead, it will be used on the employees table as a 'bridge - connector - pointer' to the person model.
    """


    base_role = Person.Role.EMPLOYEE

    class Meta:
        proxy = True

    objects = EmployeeManager()  # Custom Manager for the Employee model used only to filter the employees.


class Employee(EmployeeBridge):
    # Employee_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    # deductions = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    class EmployeeRole(models.TextChoices):
        OWNER = "OWNER", "Owner"
        MANAGER = "MANAGER", "Manager"
        CASHIER = "CASHIER", "Cashier"
        CHEF = "CHEF", "Chef"
        WAITER = "WAITER", "Waiter"
        CLEANER = "CLEANER", "Cleaner"
        # ___ = "", ""

    
    employee_role = models.CharField(max_length=50, choices=EmployeeRole.choices)

    salary = models.DecimalField(
        max_digits=10, decimal_places=2, 
        null=False, blank=False, 
        validators=[valid_salary]
        )


    class Meta:
        db_table = "employees"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


    def __str__(self):
        return self.full_name
    

    def save(self, force_update=True, commit=True, *args, **kwargs):
        """
        This method is used to set the role of the user to the base_role of the model.
        """
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        super(Person, self).save(*args, **kwargs)

