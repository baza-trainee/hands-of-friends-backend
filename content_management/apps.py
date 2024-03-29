from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class ContentManagementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "content_management"
    verbose_name = _("Content Management")
