from django.contrib import admin
from email_config.models import EmailSettings, Recipient


@admin.register(EmailSettings)
class EmailSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "backend",
        "host",
        "port",
        "host_user",
    )
    list_editable = ("host", "port", "host_user")
    readonly_fields = ("backend", "use_tls", "use_ssl")

    def has_add_permission(self, request) -> bool:
        if EmailSettings.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None) -> bool:
        return False


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("email",)
