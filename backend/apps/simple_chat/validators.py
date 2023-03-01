from django.core.exceptions import ValidationError


def validate_participants_count(value):
    if value.count() > 2:
        raise ValidationError("Count of participants is out of limit (2)")
