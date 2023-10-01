from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class PersonManager(BaseUserManager):
    """
    This is a custom manager for the Person model.
    It is used to create a Person instance.
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, and password.
        """
        if email:
            email = self.normalize_email(email)

        user = self.model(
            username=username,
            **extra_fields
        )

        if not password:
            user.set_unusable_password()  # Set the password as unusable
        else:
            user.set_password(password)
            user.save(using=self._db)
            return user
        

    def create_superuser(self, username, password=None, **extra_fields):
        
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)


        return self.create_user(username, password, **extra_fields)
