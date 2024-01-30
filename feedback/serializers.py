from rest_framework import serializers
from feedback.models import FeedbackForm


class FeedbackFormSerializer(serializers.ModelSerializer):
    sent_at = serializers.DateTimeField(read_only=True, format="%d.%m.%Y %H:%M:%S")

    class Meta:
        model = FeedbackForm
        fields = (
            "id",
            "name",
            "email",
            "phone_number",
            "message",
            "sent_at",
        )
