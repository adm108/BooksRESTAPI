from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_year(value):
    first_character = 0
    for element in value:
        if first_character == 0:
            if element not in '123456789':
                raise ValidationError(_("%(value)s is a wrong value"), params={'value': value})
            else:
                first_character == 1
                pass
        else:
            if element not in '0123456789':
                raise ValidationError(_("%(value)s is a wrong value"), params={'value': value})
            else:
                pass