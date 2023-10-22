from django.contrib.auth.backends import ModelBackend

from django.db.models import Q

from .models import Person


class CustomUserAuthenticationBackend(ModelBackend):
    """
    This is a custom authentication backend for the Person model.
    It is used to authenticate a Person instance.
    We can use this backend to authenticate a Person instance using the email, phone_number, or username.
    not only username and password.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):        
        try:
            user = Person.objects.get(Q(email=username) | Q(phone_number=username) | Q(username=username))
        except Person.DoesNotExist:
            return None
        else:
            try:
                if user.check_password(password):
                    return user
            except Exception as e:
                print(e)