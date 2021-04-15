from django.core.exceptions import ValidationError

from user.models import User


def validate_personal_number(value):
    if len(value) != 11:
        raise ValidationError('Personal Number len must be 11.')
    try:
        User.objects.get(personal_number=value)
        raise ValidationError('Personal number is already registered')
    except User.DoesNotExist:
        pass
