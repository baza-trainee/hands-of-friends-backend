from modeltranslation.translator import register, TranslationOptions
from content_management.models import (
    Tender,
    Project,
    TeamMember,
    News,
    Contacts,
    PartnerLogo,
    DonorLogo,
    ImageOrTextContent,
    HeroSlider,
    AboutUs,
    PDFReport,
)


@register(Tender)
class TenderTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(ImageOrTextContent)
class ImageOrTextContentTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ("full_name", "position")


@register(PartnerLogo)
class PartnerLogoTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(DonorLogo)
class DonorLogoTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Contacts)
class ContactsTranslationOptions(TranslationOptions):
    fields = ("address",)


@register(HeroSlider)
class HeroSliderTranslationOptions(TranslationOptions):
    fields = ("title", "alt_text")


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ("history", "principles", "values")


@register(PDFReport)
class PDFReportTranslationOptions(TranslationOptions):
    fields = ("title",)
