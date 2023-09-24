from users.managers import PersonManager
from users.models import Person   

class AdminManager(PersonManager):
    """
    This is a custom manager for the Admin model.
    It is used to filter the admins from the Person model.
    """
    def get_queryset(self):
        return super().get_queryset().filter(role=Person.Role.ADMIN)
    
    