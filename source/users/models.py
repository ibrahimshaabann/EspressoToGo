from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import PersonManager

from .validators import valid_phone_number

# from django_extensions.db.models import TimeStampedModel


class Person(AbstractBaseUser, PermissionsMixin):
    """
    This is the Person model.
    It is used to create a Person instance.
    And it is used as a base model for all app users.
    Simulates an abstract class that have all common properties of all users.
    """
    
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CUSTOMER = "CUSTOMER", "Customer"
        EMPLOYEE = "EMPLOYEE", "Employee"
        # MANAGER = "MANAGER", "Manager"
        # ___ = "", ""

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    
    full_name = models.CharField(max_length=50, blank=True, null=True)

    username = models.CharField(max_length=50, unique=True, db_index=True, null=True, blank=True)

    email = models.EmailField(unique=True, db_index=True, null=True, blank=True)

    phone_number = models.CharField(
        max_length=20, blank=True, 
        null=True, unique=True, db_index=True,
        validators=[valid_phone_number]
    )
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    
    birth_date = models.DateField(null=True, blank=True)

    objects = PersonManager()

    is_staff = models.BooleanField(default=False)    
    
    USERNAME_FIELD = "email"
    
    EMAIL_FIELD = 'username'

    REQUIRED_FIELDS = ["username"]

    def save(self, force_update=True, commit=True, *args, **kwargs):
        """
        This method is used to set the role of the user to the base_role of the model.
        """
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        super(Person, self).save(*args, **kwargs)


    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "users"


        