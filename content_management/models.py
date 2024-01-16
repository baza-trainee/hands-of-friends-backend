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
    image = models.ImageField(
        upload_to=UploadToPath("projects/"),
        validators=[validate_image],
    )
    title = models.CharField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_active"]

    def __str__(self):
        return f"{self.title}"


class TeamMember(models.Model):
    image = models.ImageField(
        upload_to=UploadToPath("team-members/"), validators=[validate_image]
    )
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_at"]
        verbose_name_plural = "team members"
        verbose_name = "team member"

    def __str__(self):
        return f"{self.full_name} [{self.position}]"
