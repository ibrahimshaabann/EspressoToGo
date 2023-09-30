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