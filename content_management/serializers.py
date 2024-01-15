from rest_framework import serializers
from cloudinary.utils import cloudinary_url

from content_management.models import Tender, Project


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
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "image",
            "description",
            "is_active",
        )

    def get_image(self, obj):
        if obj.image:
            public_id = obj.image.public_id
            url, options = cloudinary_url(public_id)
            return url
        return None
