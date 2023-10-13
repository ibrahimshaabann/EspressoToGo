from users.models import Person
from users.managers import PersonManager


class EmployeeManager(PersonManager):
    """
    This is a custom manager for the Employee model.
    It is used to filter the employees from the Person model.
    """

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=Person.Role.EMPLOYEE)