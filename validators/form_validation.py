import re
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from validators.constants import RESTRICTED_EMAIL_DOMAINS


def validate_email_domain(email: str) -> None:
    if any(email.endswith("." + domain) for domain in RESTRICTED_EMAIL_DOMAINS):
        raise ValidationError(
            f"Email addresses from these domains are not allowed: {', '.join(RESTRICTED_EMAIL_DOMAINS)}."
        )


def validate_name(name: str) -> str:
    if len(name) < 2:
        raise ValidationError(_("Name must be at least 2 characters long."))

    if len(name) > 50:
        raise ValidationError(_("Name must be at most 50 characters long."))

    return name


def validate_phone_number(phone_number: str) -> str:
    """Phone number must contain only digits, '+', '(', ')', '-' and empty space."""
    if not re.match(r"^[0-9\s+()-]+$", phone_number):
        raise ValidationError(
            "Phone number must contain only digits, '+', '(', ')', '-' and empty space."
        )

    if len(phone_number) < 6:
        raise ValidationError("Phone number must be at least 6 characters long.")

    if len(phone_number) > 30:
        raise ValidationError("Phone number must be at most 30 characters long.")

    return phone_number
