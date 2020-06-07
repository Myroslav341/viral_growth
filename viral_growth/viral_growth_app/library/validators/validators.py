from django.core.exceptions import ValidationError


def validate_password(value: str):
    if len(value) < 6:
        raise ValidationError('Password must be at least 6 characters')


def validate_unique_field(model, field: str):
    def validate_unique_model_field(value: str):
        for object in model.objects.all():
            if getattr(object, field) == value:
                raise ValidationError(f'Unique validation failed for {field}')

    return validate_unique_model_field
