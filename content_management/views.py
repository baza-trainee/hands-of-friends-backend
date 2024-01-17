from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from content_management.models import Tender, Project, TeamMember, PartnerLogo
from content_management.serializers import (
    TenderSerializer,
    ProjectSerializer,
    TeamMemberSerializer,
    PartnerLogoSerializer,
)


class BasePagination(PageNumberPagination):
    max_page_size = 100


class TenderPagination(BasePagination):
    page_size = 9


class ProjectPagination(BasePagination):
    page_size = 3


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="Accept-Language",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            required=False,
            description="Language code to get the content in a specific language (e.g., en, uk)",
            enum=["en", "uk"],
        ),
    ]
)
class TenderViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    pagination_class = TenderPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        is_active = self.request.query_params.get("is_active", None)

        if is_active is not None:
            queryset = queryset.filter(
                is_active=True if is_active.lower() == "true" else False
            )

        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "is_active",
                type=OpenApiTypes.STR,
                description="Filter by is_active field true, false (ex. ?is_active=true)",
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="Accept-Language",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            required=False,
            description="Language code to get the content in a specific language (e.g., en, uk)",
            enum=["en", "uk"],
        ),
    ]
)
class ProjectViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        is_active = self.request.query_params.get("is_active", None)

        if is_active is not None:
            queryset = queryset.filter(
                is_active=True if is_active.lower() == "true" else False
            )

        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "is_active",
                type=OpenApiTypes.STR,
                description="Filter by is_active field true, false (ex. ?is_active=true)",
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="Accept-Language",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            required=False,
            description="Language code to get the content in a specific language (e.g., en, uk)",
            enum=["en", "uk"],
        )
    ]
)
class TeamMemberViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class PartnerLogoViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PartnerLogo.objects.all()
    serializer_class = PartnerLogoSerializer
