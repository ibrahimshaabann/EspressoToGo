from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def valid_phone_number(value):

    """
    This validator checks if the phone number contains only digits.
    """

    if not value.isdigit():
        raise ValidationError(
            _("Phone number must contain only digits."),
            code='invalid'
        )