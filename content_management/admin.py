from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext as _
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

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
    HeroSlider,
    AboutUs,
)


class ImageAdminMixin:
    def image_tag(self, obj):
        if hasattr(obj, "image") and obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="auto" />')
        return "No Image"

    image_tag.short_description = _("Image Preview")


@admin.register(Tender)
class TenderAdmin(TranslationAdmin):
    list_display = ("title", "start_date", "end_date", "is_shown")
    list_filter = ("title", "start_date", "end_date")
    exclude = ("is_active",)
    group_fieldsets = True


class ImageOrTextContentInline(TranslationStackedInline):
    model = ImageOrTextContent
    extra = 1


@admin.register(Project)
class ProjectAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("title", "image_tag", "is_shown")
    list_filter = ("is_active", "is_shown")
    inlines = (ImageOrTextContentInline,)
    exclude = ("is_active",)
    search_fields = ("title",)
    group_fieldsets = True


@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("full_name", "position", "image_tag")
    list_filter = ("position",)
    search_fields = ("full_name", "position")


@admin.register(PartnerLogo)
class PartnerLogoAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("name", "image_tag")
    search_fields = ("name",)


@admin.register(DonorLogo)
class DonorLogoAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("name", "image_tag")
    search_fields = ("name",)


@admin.register(News)
class NewsAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("title", "date", "image_tag")
    list_filter = ("date",)
    search_fields = ("title", "date")
    group_fieldsets = True


@admin.register(PDFReport)
class PDFReportAdmin(TranslationAdmin):
    """PDFReport Admin"""

    list_display = ("title", "file_url", "added_at")


@admin.register(Contacts)
class ContactsAdmin(TranslationAdmin):
    """Contacts Admin with singleton pattern"""

    list_display = ("phone_number", "email", "youtube_link", "facebook_link", "address")

    def has_add_permission(self, request, obj=None):
        if Contacts.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroSlider)
class HeroSliderAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("title", "image_tag")

    def has_add_permission(self, request, obj=None):
        if HeroSlider.objects.count() == 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if HeroSlider.objects.count() <= 1:
            return False


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    list_display = ("display_custom_text",)
    group_fieldsets = True

    def display_custom_text(self, obj) -> str:
        return "Редагувати текст про нас"

    display_custom_text.short_description = "Текст про нас"

    def get_actions(self, request):
        # Disable all actions
        return None

    def has_add_permission(self, request, obj=None):
        if AboutUs.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False
