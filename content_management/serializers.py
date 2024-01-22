from rest_framework import serializers

from content_management.models import Tender, Project, TeamMember, PartnerLogo, News


class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = (
            "id",
            "title",
            "description",
            "date",
            "is_active",
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "image",
            "description",
            "is_active",
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
            "link_to_news",
        )
