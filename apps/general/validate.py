from django.core.exceptions import ValidationError


def phone_number_validate(phone_number: str):
    if len(phone_number) != 13 or not phone_number.startswith('+998') or not phone_number[1:].isdigit():
        raise ValidationError('phone number is not valid.')


def normalize_text(obj):
    for i in obj.fields():
        field = getattr(obj, i)
        setattr(obj, i, ''.join(field.split()))
    return obj