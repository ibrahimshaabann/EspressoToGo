from django.contrib.auth.backends import ModelBackend

from django.db.models import Q

from .models import Person


class CustomUserAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Person.objects.get(Q(email=username) | Q(phone_number=username))
        except Person.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user