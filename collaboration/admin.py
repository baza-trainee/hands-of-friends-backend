from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from collaboration.models import DonorForm, PartnerForm, VolunteerForm


@admin.register(PartnerForm)
class PartnerFormAdmin(ImportExportModelAdmin):
    list_display = ("organization_name", "message", "sent_at")
    list_display_links = ("organization_name", "message", "sent_at")
    search_fields = ("organization_name", "sent_at")
    list_filter = ("sent_at",)

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
        return super(PartnerFormAdmin, self).changeform_view(
            request, object_id, form_url, extra_context
        )


@admin.register(DonorForm)
class DonorFormAdmin(ImportExportModelAdmin):
    list_display = ("organization_name", "message", "sent_at")
    list_display_links = ("organization_name", "message", "sent_at")
    search_fields = ("organization_name", "sent_at")
    list_filter = ("sent_at",)

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
        return super(DonorFormAdmin, self).changeform_view(
            request, object_id, form_url, extra_context
        )


@admin.register(VolunteerForm)
class VolunteerFormAdmin(ImportExportModelAdmin):
    list_display = ("name", "phone", "message", "sent_at")
    list_display_links = ("name", "phone", "message", "sent_at")
    search_fields = ("name", "sent_at")
    list_filter = ("sent_at",)

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
        return super(VolunteerFormAdmin, self).changeform_view(
            request, object_id, form_url, extra_context
        )
