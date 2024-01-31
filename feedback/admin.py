from django.contrib import admin

from feedback.models import FeedbackForm


@admin.register(FeedbackForm)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "sent_at")

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def get_readonly_fields(self, request, obj=None) -> list:
        return [f.name for f in self.model._meta.fields]

    def changeform_view(
        self, request, object_id=None, form_url="", extra_context=None
    ) -> None:
        extra_context = extra_context or {}
        extra_context["show_save_and_continue"] = False
        extra_context["show_save"] = False
        return super(FeedbackFormAdmin, self).changeform_view(
            request, object_id, form_url, extra_context
        )
