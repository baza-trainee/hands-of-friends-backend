from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from content_management.models import Tender, Project


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
