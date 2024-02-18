from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EmailConfigConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "email_config"
    verbose_name = _("Email Configuration")
