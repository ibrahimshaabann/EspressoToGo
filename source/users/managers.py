# from django.contrib.auth.models import BaseUserManager
# from django.utils import timezone


# class PersonManager(BaseUserManager):
#     """
#     This is a custom manager for the Person model.
#     It is used to create a Person instance.
#     """

#     def create_user(self, username, password=None, **extra_fields):
#         """
#         Creates and saves a User with the given username, and password.
#         """
#         if email:
#             email = self.normalize_email(email)

#         user = self.model(
#             username=username,
#             **extra_fields
#         )

#         if not password:
#             user.set_unusable_password()  # Set the password as unusable
#         else:
#             user.set_password(password)
#             user.save(using=self._db)
#             return user
        

#     def create_superuser(self, username, password=None, **extra_fields):
        
        
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)


#         return self.create_user(username, password, **extra_fields)


from django.contrib.auth.models import BaseUserManager

class PersonManager(BaseUserManager):
    def create_user(self, email, full_name, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            full_name=full_name,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, full_name, phone_number, password, **extra_fields)
