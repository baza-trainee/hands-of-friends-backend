from rest_framework import routers

from content_management.views import (
    TenderViewSet,
    ProjectViewSet,
    TeamMemberViewSet,
    PartnerLogoViewSet,
    NewsViewSet,
    ContactsViewSet,
)

router = routers.DefaultRouter()
router.register("tenders", TenderViewSet)
router.register("projects", ProjectViewSet)
router.register("team", TeamMemberViewSet)
router.register("partners", PartnerLogoViewSet)
router.register("news", NewsViewSet)
router.register("contacts", ContactsViewSet)

urlpatterns = router.urls

app_name = "content_management"
