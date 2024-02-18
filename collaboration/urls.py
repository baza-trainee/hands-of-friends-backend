from rest_framework import routers

from collaboration.views import (
    PartnerFormViewSet,
    DonorFormViewSet,
    VolunteerFormViewSet,
)

router = routers.DefaultRouter()
router.register(r"partner-form", PartnerFormViewSet)
router.register(r"donor-form", DonorFormViewSet)
router.register(r"volunteer-form", VolunteerFormViewSet)

urlpatterns = router.urls

app_name = "collaboration"
