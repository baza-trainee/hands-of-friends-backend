from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext as _
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from content_management.models import (
    Tender,
    Project,
    ImageOrTextContent,
    TeamMember,
    PartnerLogo,
    News,
    Contacts,
    PDFReport,
    DonorLogo,
)


class ImageAdminMixin:
    def image_tag(self, obj):
        if hasattr(obj, "image") and obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="auto" />')
        return "No Image"

    image_tag.short_description = _("Image Preview")


@admin.register(Tender)
class TenderAdmin(TabbedTranslationAdmin):
    list_display = ("title", "start_date", "end_date", "is_shown")
    list_filter = ("title", "start_date", "end_date")
    exclude = ("is_active",)
    search_fields = ("title", "date")
    group_fieldsets = True


class ImageOrTextContentInline(TranslationStackedInline):
    model = ImageOrTextContent
    extra = 1


@admin.register(Project)
class ProjectAdmin(TabbedTranslationAdmin, ImageAdminMixin):
    list_display = ("title", "image_tag", "is_shown")
    list_filter = ("is_active", "is_shown")
    inlines = (ImageOrTextContentInline,)
    exclude = ("is_active",)
    search_fields = ("title",)
    group_fieldsets = True


@admin.register(TeamMember)
class TeamMemberAdmin(TabbedTranslationAdmin, ImageAdminMixin):
    list_display = ("full_name", "position", "image_tag")
    list_filter = ("position",)
    search_fields = ("full_name", "position")


@admin.register(PartnerLogo)
class PartnerLogoAdmin(TabbedTranslationAdmin, ImageAdminMixin):
    list_display = ("company_name", "image_tag")
    search_fields = ("company_name",)


@admin.register(DonorLogo)
class DonorLogoAdmin(TabbedTranslationAdmin, ImageAdminMixin):
    list_display = ("name", "image_tag")
    search_fields = ("name",)


@admin.register(News)
class NewsAdmin(TabbedTranslationAdmin, ImageAdminMixin):
    list_display = ("title", "date", "image_tag")
    list_filter = ("date",)
    search_fields = ("title", "date")
    group_fieldsets = True


@admin.register(PDFReport)
class PDFReportAdmin(admin.ModelAdmin):
    """PDFReport Admin"""

    list_display = ("title", "file_url", "added_at")


@admin.register(Contacts)
class ContactsAdmin(TabbedTranslationAdmin):
    """Contacts Admin with singleton pattern"""

    list_display = ("phone_number", "email", "youtube_link", "facebook_link", "address")

    def has_add_permission(self, request, obj=None):
        if Contacts.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False
