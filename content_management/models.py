from django.db import models

from content_management.validators import validate_image
from cloudinary.models import CloudinaryField


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
    image = CloudinaryField("image", validators=[validate_image])
    title = models.CharField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_active"]

    def __str__(self):
        return f"{self.title}"
