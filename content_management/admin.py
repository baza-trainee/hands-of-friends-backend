from django.contrib import admin

from content_management.models import Tender


class TenderAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_active")
    list_filter = ("title", "is_active", "date")
    search_fields = ("title", "date")


admin.site.register(Tender, TenderAdmin)
