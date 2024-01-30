from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from feedback.models import FeedbackForm
from feedback.serializers import FeedbackFormSerializer


class FeedbackFormViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = FeedbackForm.objects.all()
    serializer_class = FeedbackFormSerializer
