from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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

    def validate(self, data):
        request = self.context["request"]
        if request.content_type != "application/json":
            raise ValidationError("Content-Type must be 'application/json'.")
        return data
