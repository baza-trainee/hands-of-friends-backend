import re
from django.core.exceptions import ValidationError


def validate_phone_number(phone_number: str) -> None:
    if not re.match(r"^\+\d{1,3}\s?\d{4,14}$", phone_number):
        raise ValidationError(
            "Enter a valid international phone number (e.g., +1234567890)."
        )
