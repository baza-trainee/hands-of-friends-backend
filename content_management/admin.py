from django.contrib import admin
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin

from content_management.models import Tender, Project, TeamMember, PartnerLogo


class ImageAdminMixin:
    def image_tag(self, obj):
        if hasattr(obj, "image") and obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="auto" />')
        return "No Image"

    image_tag.short_description = "Image Preview"


@admin.register(Tender)
class TenderAdmin(TranslationAdmin):
    list_display = ("title", "date", "is_active")
    list_filter = ("title", "is_active", "date")
    search_fields = ("title", "date")
    group_fieldsets = True


@admin.register(Project)
class ProjectAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("title", "is_active", "image_tag")
    list_filter = ("title", "is_active")
    search_fields = ("title",)
    group_fieldsets = True


@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin, ImageAdminMixin):
    list_display = ("full_name", "position", "image_tag")
    list_filter = ("full_name", "position")
    search_fields = ("full_name", "position")
    group_fieldsets = True


@admin.register(PartnerLogo)
class PartnerLogoAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = (
        "id",
        "image_tag",
    )
    search_fields = ("id",)
