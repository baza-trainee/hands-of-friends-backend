from django.db import models
from validators.feedback_form_validation import (
    validate_email_domain,
    validate_name,
)


class FeedbackForm(models.Model):
    name = models.CharField(max_length=50, validators=[validate_name])
    email = models.EmailField(validators=[validate_email_domain])
    phone_number = models.CharField(max_length=30)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-sent_at",)

    def __str__(self) -> str:
        return f"Feedback from {self.name} at {self.sent_at}"

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)
