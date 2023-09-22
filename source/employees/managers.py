from users.models import Person
from users.managers import PersonManager


class EmployeeManager(PersonManager):

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=Person.Role.EMPLOYEE)