from rest_framework import routers

from content_management.views import TenderViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register("tenders", TenderViewSet)
router.register("projects", ProjectViewSet)

urlpatterns = router.urls

app_name = "content_management"
