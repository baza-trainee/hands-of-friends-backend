from modeltranslation.translator import register, TranslationOptions
from content_management.models import Tender, Project


@register(Tender)
class TenderTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("title", "description")
