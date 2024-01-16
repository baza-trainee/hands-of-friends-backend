from rest_framework import routers

from content_management.views import (
    TenderViewSet,
    ProjectViewSet,
    TeamMemberViewSet,
    PartnerLogoViewSet,
)

router = routers.DefaultRouter()
router.register("tenders", TenderViewSet)
router.register("projects", ProjectViewSet)
router.register("team", TeamMemberViewSet)
router.register("partners", PartnerLogoViewSet)

urlpatterns = router.urls

app_name = "content_management"
