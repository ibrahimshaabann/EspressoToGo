from django.contrib.auth.base_user import BaseUserManager


class PersonManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        try:
            if not email:
                raise ValueError("The Email field must be set")
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()

            return user
        
        except Exception as e:
            raise e


    def create_superuser(self, email, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        

        return self.create_user(email, password, phone_number=phone_number, **extra_fields)
