from django.db import models
from django.utils.translation import gettext_lazy as _
from validators.form_validation import (
    validate_email_domain,
    validate_name,
    validate_phone_number,
)


class PartnerForm(models.Model):
    organization_name = models.CharField(_("Organization Name"), max_length=255)
    representative_name = models.CharField(
        _("Representative Name"), max_length=50, validators=[validate_name]
    )
    email = models.EmailField(_("Email"), validators=[validate_email_domain])
    phone = models.CharField(
        _("Phone"), max_length=30, validators=[validate_phone_number]
    )
    message = models.TextField(max_length=300, verbose_name=_("Message"))
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Sent at"))

    class Meta:
        ordering = ("-sent_at",)
        verbose_name = _("Partner form")
        verbose_name_plural = _("Partners forms")

    def __str__(self) -> str:
        return str(_(f"Feedback from {self.organization_name} at {self.sent_at}"))


class DonorForm(models.Model):
    organization_name = models.CharField(_("Organization Name"), max_length=255)
    representative_name = models.CharField(
        _("Representative Name"), max_length=50, validators=[validate_name]
    )
    email = models.EmailField(_("Email"), validators=[validate_email_domain])
    phone = models.CharField(
        _("Phone"), max_length=30, validators=[validate_phone_number]
    )
    message = models.TextField(max_length=300, verbose_name=_("Message"))
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Sent at"))

    class Meta:
        ordering = ("-sent_at",)
        verbose_name = _("Donor form")
        verbose_name_plural = _("Donor forms")

    def __str__(self) -> str:
        return str(_(f"Feedback from {self.organization_name} at {self.sent_at}"))


class VolunteerForm(models.Model):
    name = models.CharField(_("Name"), max_length=50, validators=[validate_name])
    city = models.CharField(_("City"), max_length=255)
    email = models.EmailField(_("Email"), validators=[validate_email_domain])
    phone = models.CharField(
        _("Phone"), max_length=30, validators=[validate_phone_number]
    )
    message = models.TextField(max_length=300, verbose_name=_("Message"))
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Sent at"))

    class Meta:
        ordering = ("-sent_at",)
        verbose_name = _("Volunteer form")
        verbose_name_plural = _("Volunteer forms")

    def __str__(self) -> str:
        return str(_(f"Feedback from {self.name} at {self.sent_at}"))
