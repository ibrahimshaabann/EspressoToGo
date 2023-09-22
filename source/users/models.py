from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import PersonManager

from .validators import valid_phone_number

# from django_extensions.db.models import TimeStampedModel


class Person(AbstractBaseUser, PermissionsMixin):
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

    # Add related_name to avoid clashes with auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='person_set',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='person_set',
    )
    
    USERNAME_FIELD = "username"

    class Meta:
        db_table = "users"