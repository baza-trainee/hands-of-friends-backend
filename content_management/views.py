from django.utils import timezone
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
    PDFReport,
    DonorLogo,
    HeroSlider,
    AboutUs,
)
from content_management.serializers import (
    TenderSerializer,
    ProjectSerializer,
    TeamMemberSerializer,
    PartnerLogoSerializer,
    NewsSerializer,
    ContactsSerializer,
    PDFReportSerializer,
    DonorLogoSerializer,
    HeroSliderSerializer,
    AboutUsSerializer,
)


class BasePagination(PageNumberPagination):
    max_page_size = 100


class DynamicPagination(PageNumberPagination):
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

        end_date = self.request.query_params.get("end_date", None)
        if end_date is not None:
            queryset = queryset.filter(
                end_date__lt=timezone.now().update(is_active=False)
            )

        is_active = self.request.query_params.get("is_active", None)
        is_shown = self.request.query_params.get("is_shown", None)

        if is_active is not None:
            queryset = queryset.filter(
                is_active=True if is_active.lower() == "true" else False
            )

        if is_shown is not None:
            queryset = queryset.filter(
                is_shown=True if is_shown.lower() == "true" else False
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
                "is_shown",
                type=OpenApiTypes.STR,
                description="Filter by is_shown field true, false (ex. ?is_shown=true)",
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
        ),
    ]
)
class ProjectViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        end_date = self.request.query_params.get("end_date", None)
        if end_date is not None:
            queryset = queryset.filter(
                end_date__lt=timezone.now().update(is_active=False)
            )

        is_active = self.request.query_params.get("is_active", None)
        is_shown = self.request.query_params.get("is_shown", None)

        if is_active is not None:
            queryset = queryset.filter(
                is_active=True if is_active.lower() == "true" else False
            )

        if is_shown is not None:
            queryset = queryset.filter(
                is_shown=True if is_shown.lower() == "true" else False
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
                "is_shown",
                type=OpenApiTypes.STR,
                description="Filter by is_shown field true, false (ex. ?is_shown=true)",
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
class DonorLogoViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = DonorLogo.objects.all()
    serializer_class = DonorLogoSerializer


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
    pagination_class = DynamicPagination


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
class PDFReportView(mixins.ListModelMixin, GenericViewSet):
    queryset = PDFReport.objects.all()
    serializer_class = PDFReportSerializer


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
class HeroSliderViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = HeroSlider.objects.all()
    serializer_class = HeroSliderSerializer


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
class AboutUsViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
