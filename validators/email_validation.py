from django.core.exceptions import ValidationError
from validators.constants import RESTRICTED_EMAIL_DOMAINS


def validate_email_domain(email: str) -> None:
    if any(email.endswith("." + domain) for domain in RESTRICTED_EMAIL_DOMAINS):
        raise ValidationError(
            f"Email addresses from these domains are not allowed: {', '.join(RESTRICTED_EMAIL_DOMAINS)}."
        )


def validate_name(name: str) -> str:
    if not name.isalpha():
        raise ValidationError("Name must contain only letters.")

    if len(name) < 2:
        raise ValidationError("Name must be at least 2 characters long.")

    if len(name) > 50:
        raise ValidationError("Name must be at most 50 characters long.")

    return name
