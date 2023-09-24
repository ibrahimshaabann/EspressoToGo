from django.contrib.auth.base_user import BaseUserManager


class PersonManager(BaseUserManager):
    def create_user(self, **extra_fields):
        pass


    def create_superuser(self, **extra_fields):
        pass