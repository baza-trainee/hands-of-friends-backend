from rest_framework import serializers

from content_management.models import (
    Tender,
    Project,
    TeamMember,
    PartnerLogo,
    DonorLogo,
    News,
    Contacts,
    PDFReport,
    ImageOrTextContent,
    HeroSlider,
    AboutUs,
)


class TenderSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%d.%m.%Y")
    end_date = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Tender
        fields = (
            "id",
            "title",
            "description",
            "start_date",
            "end_date",
            "is_active",
            "is_shown",
        )


class ImageOrTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageOrTextContent
        fields = (
            "id",
            "image",
            "text",
        )


class ProjectSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%d.%m.%Y")
    end_date = serializers.DateField(format="%d.%m.%Y")
    content = ImageOrTextSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "image",
            "description",
            "start_date",
            "end_date",
            "is_active",
            "is_shown",
            "content",
        )


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = (
            "id",
            "image",
            "full_name",
            "position",
        )


class PartnerLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerLogo
        fields = (
            "id",
            "image",
            "name",
        )


class DonorLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorLogo
        fields = (
            "id",
            "image",
            "name",
        )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "image",
            "date",
            "title",
            "description",
        )


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = (
            "id",
            "phone_number",
            "email",
            "youtube_link",
            "facebook_link",
            "address",
        )


class PDFReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFReport
        fields = (
            "id",
            "title",
            "file_url",
            "added_at",
        )


class HeroSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlider
        fields = (
            "id",
            "title",
            "image",
            "alt_text",
        )


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ("id", "history", "principles", "values")
