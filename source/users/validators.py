from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def valid_phone_number(value):
    """
    This validator checks if the phone number contains only digits.
    """

    phone_number_pattern = r'^/d{11}$'
    if not re.match(phone_number_pattern, value):
        raise ValidationError(
            _("(Phone number must contain only digits and length of 11 digits."),
            code='invalid'
        )

    