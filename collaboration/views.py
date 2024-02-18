from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from collaboration.models import PartnerForm, DonorForm, VolunteerForm
from collaboration.serializers import (
    PartnerFormSerializer,
    DonorFormSerializer,
    VolunteerFormSerializer,
)


class PartnerFormViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = PartnerForm.objects.all()
    serializer_class = PartnerFormSerializer

    def create(self, request, *args, **kwargs):
        if request.content_type != "application/json":
            return Response(
                {"error": "Invalid Content-Type header. Expected 'application/json'."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().create(request, *args, **kwargs)


class DonorFormViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = DonorForm.objects.all()
    serializer_class = DonorFormSerializer

    def create(self, request, *args, **kwargs):
        if request.content_type != "application/json":
            return Response(
                {"error": "Invalid Content-Type header. Expected 'application/json'."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().create(request, *args, **kwargs)


class VolunteerFormViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = VolunteerForm.objects.all()
    serializer_class = VolunteerFormSerializer

    def create(self, request, *args, **kwargs):
        if request.content_type != "application/json":
            return Response(
                {"error": "Invalid Content-Type header. Expected 'application/json'."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().create(request, *args, **kwargs)
