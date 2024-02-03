from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from feedback.models import FeedbackForm
from feedback.serializers import FeedbackFormSerializer


class FeedbackFormViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = FeedbackForm.objects.all()
    serializer_class = FeedbackFormSerializer

    def create(self, request, *args, **kwargs):
        if request.content_type != "application/json":
            return Response(
                {"error": "Invalid Content-Type header. Expected 'application/json'."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().create(request, *args, **kwargs)
