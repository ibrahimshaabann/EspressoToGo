from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def valid_salary(value):

    """
    This validator checks if the salary is valid.
    """

    if not value.isdigit() or value < 0:
        raise ValidationError(
            _("salary must contain only digits and only postsive number."),
            code='invalid'
        )