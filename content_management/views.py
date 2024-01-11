from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from content_management.models import Tender
from content_management.serializers import TenderSerializer


class TenderPagination(PageNumberPagination):
    page_size = 9
    max_page_size = 100


class TenderViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    pagination_class = TenderPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        is_active = self.request.query_params.get("is_active", None)

        if is_active is not None:
            queryset = queryset.filter(is_active=True if is_active == "true" else False)

        return queryset
