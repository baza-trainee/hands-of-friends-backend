from django.db import models
from validators.feedback_form_validation import (
    validate_email_domain,
    validate_name,
    validate_phone_number,
)


class FeedbackForm(models.Model):
    name = models.CharField(validators=[validate_name])
    email = models.EmailField(validators=[validate_email_domain])
    phone_number = models.CharField(validators=[validate_phone_number])
    message = models.TextField(max_length=300)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-sent_at",)

    def __str__(self) -> str:
        return f"Feedback from {self.name} at {self.sent_at}"

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)
