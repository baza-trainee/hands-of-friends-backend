from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CollaborationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "collaboration"
    verbose_name = _("Collaboration")

    def ready(self):
        import email_config.send_notifications
