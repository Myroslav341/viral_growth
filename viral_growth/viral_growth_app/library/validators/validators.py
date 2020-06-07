from typing import Callable
from django.core.exceptions import ValidationError


def validate_password(value: str):
    """
    validate password
    :raises ValidationError: if validation failed
    """
    if len(value) < 6:
        raise ValidationError('Password must be at least 6 characters')


def validate_unique_field(model, field: str) -> Callable[[str], None]:
    """
    generate validate function for field unique check
    :params model: model to check
    :params field: field in model to check
    :return: validate function
    """
    def validate_unique_model_field(value: str):
        """
        check field unique
        :params value: value to check
        :raises ValidationError: if validation failed
        """
        for object in model.objects.all():
            if getattr(object, field) == value:
                raise ValidationError(f'Unique validation failed for {field}')

    return validate_unique_model_field
