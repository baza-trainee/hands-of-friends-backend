from rest_framework import routers

from feedback.views import FeedbackFormViewSet

router = routers.DefaultRouter()
router.register("feedback", FeedbackFormViewSet)

urlpatterns = router.urls

app_name = "feedback"
