from rest_framework import routers

from content_management.views import (
    TenderViewSet,
    ProjectViewSet,
    TeamMemberViewSet,
    PartnerLogoViewSet,
    DonorLogoViewSet,
    NewsViewSet,
    ContactsViewSet,
    PDFReportView,
)

router = routers.DefaultRouter()
router.register("tenders", TenderViewSet)
router.register("projects", ProjectViewSet)
router.register("team", TeamMemberViewSet)
router.register("partners", PartnerLogoViewSet)
router.register("donors", DonorLogoViewSet)
router.register("news", NewsViewSet)
router.register("contacts", ContactsViewSet)
router.register("pdf-report", PDFReportView)

urlpatterns = router.urls

app_name = "content_management"
