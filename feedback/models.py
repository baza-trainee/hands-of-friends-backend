from django.db import models
from validators.form_validation import (
    validate_email_domain,
    validate_name,
    validate_phone_number,
)
from django.utils.translation import gettext_lazy as _


class FeedbackForm(models.Model):
    name = models.CharField(validators=[validate_name], verbose_name=_("Name"))
    email = models.EmailField(
        validators=[validate_email_domain], verbose_name=_("Email")
    )
    phone_number = models.CharField(
        validators=[validate_phone_number], verbose_name=_("Phone number")
    )
    message = models.TextField(max_length=300, verbose_name=_("Message"))
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Sent at"))

    class Meta:
        ordering = ("-sent_at",)
        verbose_name = _("Feedback form")
        verbose_name_plural = _("Feedback forms")

    def __str__(self) -> str:
        return str(_(f"Feedback from {self.name} at {self.sent_at}"))

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)
