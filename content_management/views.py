from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from content_management.models import (
    Tender,
    Project,
    TeamMember,
    PartnerLogo,
    News,
    Contacts,
)
from content_management.serializers import (
    TenderSerializer,
    ProjectSerializer,
    TeamMemberSerializer,
    PartnerLogoSerializer,
    NewsSerializer,
    ContactsSerializer,
)


class BasePagination(PageNumberPagination):
    max_page_size = 100


class ProjectPagination(PageNumberPagination):
    max_page_size = 100
    page_size_query_param = "limit"

    def get_page_size(self, request):
        limit = request.query_params.get(self.page_size_query_param)
        if limit:
            try:
                return min(int(limit), self.max_page_size)
            except ValueError:
                pass
        return super().get_page_size(request)


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
class ProjectViewSet(mixins.ListModelMixin, GenericViewSet):
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
            ),
            OpenApiParameter(
                name="limit",
                type=OpenApiTypes.INT,
                description="Number of results to return per page (ex. ?limit=2)",
            ),
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
class NewsViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


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
class ContactsViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
