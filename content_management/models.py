from django.db import models

from content_management.validators import validate_image
from content_management.upload_to_path import UploadToPath


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
    title = models.CharField()
    image = models.ImageField(
        upload_to=UploadToPath("project-images/"), validators=[validate_image]
    )
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_active"]

    def __str__(self):
        return f"{self.title}"
