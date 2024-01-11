from rest_framework import routers

from content_management.views import TenderViewSet

router = routers.DefaultRouter()
router.register("tenders", TenderViewSet)

urlpatterns = router.urls

app_name = "content_management"
