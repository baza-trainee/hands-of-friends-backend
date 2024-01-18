from django.core.exceptions import ValidationError
from django.db import models

from content_management.upload_to_path import UploadToPath
from content_management.validators import validate_image


class Tender(models.Model):
    title = models.CharField()
    description = models.TextField()
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-is_active"]

    def __str__(self):
        return f"{self.title} [{self.date}]"


class Project(models.Model):
    image = models.FileField(upload_to=UploadToPath("projects/"))
    title = models.CharField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_active", "-created_at"]

    def clean(self):
        try:
            validate_image(self.image)
        except ValidationError as e:
            raise ValidationError({"image": e})

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.full_clean()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.title}"


class TeamMember(models.Model):
    image = models.FileField(upload_to=UploadToPath("team-members/"))
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_at"]
        verbose_name_plural = "team members"
        verbose_name = "team member"

    def clean(self):
        try:
            validate_image(self.image)
        except ValidationError as e:
            raise ValidationError({"image": e})

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.full_clean()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.full_name} [{self.position}]"


class PartnerLogo(models.Model):
    company_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    image = models.FileField(upload_to=UploadToPath("partner-logos/"))
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["company_name"]
        verbose_name_plural = "partner logos"
        verbose_name = "partner logo"

    def clean(self):
        try:
            validate_image(self.image)
        except ValidationError as e:
            raise ValidationError({"image": e})

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.full_clean()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.company_name} logo"
