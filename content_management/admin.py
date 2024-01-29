from django.contrib import admin
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin

from content_management.models import (
    Tender,
    Project,
    TeamMember,
    PartnerLogo,
    News,
    Contacts,
    PDFReport,
)


class ImageAdminMixin:
    def image_tag(self, obj):
        if hasattr(obj, "image") and obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="auto" />')
        return "No Image"

    image_tag.short_description = "Image Preview"


@admin.register(Tender)
class TenderAdmin(TranslationAdmin):
    list_display = ("title", "start_date", "is_active")
    list_filter = ("title", "is_active", "start_date", "end_date")
    search_fields = ("title", "date")
    group_fieldsets = True


@admin.register(Project)
class ProjectAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("title", "is_active", "image_tag")
    list_filter = ("is_active",)
    search_fields = ("title",)
    group_fieldsets = True


@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("full_name", "position", "image_tag")
    list_filter = ("position",)
    search_fields = ("full_name", "position")
    group_fieldsets = True


@admin.register(PartnerLogo)
class PartnerLogoAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = (
        "company_name",
        "image_tag",
    )
    search_fields = ("company_name",)


@admin.register(News)
class NewsAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("title", "date", "image_tag")
    list_filter = ("date",)
    search_fields = ("title", "date")
    group_fieldsets = True


@admin.register(Contacts)
class ContactsAdmin(TranslationAdmin):
    """Contacts Admin with singleton pattern"""

    list_display = ("phone_number", "email", "youtube_link", "facebook_link", "address")
    group_fieldsets = True

    def has_add_permission(self, request, obj=None):
        if Contacts.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PDFReport)
class PDFReportAdmin(admin.ModelAdmin):
    """PDFReport Admin with singleton pattern"""

    list_display = ("title", "file_url", "added_at")

    def has_add_permission(self, request, obj=None):
        if PDFReport.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False
