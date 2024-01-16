from rest_framework import routers

from content_management.views import TenderViewSet, ProjectViewSet, TeamMemberViewSet

router = routers.DefaultRouter()
router.register("tenders", TenderViewSet)
router.register("projects", ProjectViewSet)
router.register("team", TeamMemberViewSet)

urlpatterns = router.urls

app_name = "content_management"
