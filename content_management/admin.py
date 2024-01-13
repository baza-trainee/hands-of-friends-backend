from django.contrib import admin

from content_management.models import Tender, Project


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_active")
    list_filter = ("title", "is_active", "date")
    search_fields = ("title", "date")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("title", "is_active")
    search_fields = ("title",)
