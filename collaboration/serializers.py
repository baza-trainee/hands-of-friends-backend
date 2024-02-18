from rest_framework import serializers
from collaboration.models import PartnerForm, DonorForm, VolunteerForm


class PartnerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerForm
        fields = "__all__"


class DonorFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorForm
        fields = "__all__"


class VolunteerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerForm
        fields = "__all__"
