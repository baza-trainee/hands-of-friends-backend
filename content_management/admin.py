from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from content_management.models import Tender, Project, TeamMember, PartnerLogo


@admin.register(Tender)
class TenderAdmin(TranslationAdmin):
    list_display = ("title", "date", "is_active")
    list_filter = ("title", "is_active", "date")
    search_fields = ("title", "date")
    group_fieldsets = True


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ("title", "is_active")
    list_filter = ("title", "is_active")
    search_fields = ("title",)
    group_fieldsets = True


@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ("full_name", "position")
    list_filter = ("full_name", "position")
    search_fields = ("full_name", "position")
    group_fieldsets = True


@admin.register(PartnerLogo)
class PartnerLogoAdmin(admin.ModelAdmin):
    list_display = ("id", "image",)
    search_fields = ("id",)
