from rest_framework import serializers

from content_management.models import Tender


class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = (
            "id",
            "title",
            "main_text",
            "date",
            "is_active",
        )
