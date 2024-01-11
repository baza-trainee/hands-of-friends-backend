from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from content_management.models import Tender
from content_management.serializers import TenderSerializer


class TenderViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        is_active = self.request.query_params.get("is_active", None)

        if is_active is not None:
            queryset = queryset.filter(is_active=True if is_active == "true" else False)

        return queryset
