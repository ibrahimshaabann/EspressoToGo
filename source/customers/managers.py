from users.models import Person
from users.managers import PersonManager


class CustomerManager(PersonManager):

    """
    This is a custom manager for the Customer model.
    It is used to filter the Customer from the Person model.
    """

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=Person.Role.CUSTOMER)