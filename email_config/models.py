from django.db import models
from django.utils.translation import gettext_lazy as _


class EmailSettings(models.Model):
    backend = models.CharField(
        max_length=100,
        default="email_config.backends.CustomEmailBackend",
        verbose_name=_("Backend"),
    )
    host = models.CharField(
        max_length=100, default="smtp.gmail.com", verbose_name=_("Host")
    )
    port = models.IntegerField(default=587, verbose_name=_("Port"))
    use_tls = models.BooleanField(default=True, verbose_name=_("Use TLS"))
    host_user = models.EmailField(verbose_name=_("Email"))
    host_password = models.CharField(max_length=100, verbose_name=_("Password"))
    use_ssl = models.BooleanField(default=False, verbose_name=_("Use SSL"))

    class Meta:
        verbose_name = _("Email Settings")
        verbose_name_plural = "Email Settings"

    def __str__(self):
        return "Email Settings"


class Recipient(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = _("Recipient")
        verbose_name_plural = _("Recipients")

    def __str__(self):
        return self.email
