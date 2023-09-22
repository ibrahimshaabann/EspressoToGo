from django.db import models

from django.db import models

from users.models import Person

from .managers import EmployeeManager

import uuid


class EmployeeBridge(Person):
    base_role = Person.Role.EMPLOYEE

    class Meta:
        proxy = True

    objects = EmployeeManager()


class Employee(EmployeeBridge):
    # Employee_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    # deductions = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    class Meta:
        db_table = "employees"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
    
    def __str__(self):
        return self.full_name