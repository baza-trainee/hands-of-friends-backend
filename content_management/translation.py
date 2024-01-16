from modeltranslation.translator import register, TranslationOptions
from content_management.models import Tender, Project, TeamMember


@register(Tender)
class TenderTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ("full_name", "position")
