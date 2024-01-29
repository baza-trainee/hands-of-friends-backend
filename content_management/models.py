from django.core.exceptions import ValidationError
from django.db import models

from content_management.upload_to_path import UploadToPath
from validators.image_validation import validate_and_convert_image
from validators.pdf_validation import validate_pdf_file
from ckeditor.fields import RichTextField


class Singleton(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise Exception(f"Only one {self.__class__.__name__} instance is allowed.")
        super().save(*args, **kwargs)


class Tender(models.Model):
    title = models.CharField()
    description = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_active", "-start_date"]

    def __str__(self):
        return f"{self.title} ({self.start_date} - {self.end_date})"


class Project(models.Model):
    image = models.FileField(upload_to="projects/")
    title = models.CharField()
    description = RichTextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_active", "-created_at"]

    def __str__(self):
        return f"{self.title}"

    def clean(self):
        try:
            validate_and_convert_image(self.image)
        except ValidationError as e:
            raise ValidationError({"image": e})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class TeamMember(models.Model):
    image = models.FileField(upload_to="team-members/")
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_at"]
        verbose_name_plural = "team members"
        verbose_name = "team member"

    def __str__(self):
        return f"{self.full_name} ({self.position})"

    def clean(self):
        try:
            validate_and_convert_image(self.image)
        except ValidationError as e:
            raise ValidationError({"image": e})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class PartnerLogo(models.Model):
    image = models.FileField(upload_to="partner-logos/")
    company_name = models.CharField(unique=True, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["company_name"]
        verbose_name_plural = "partner logos"
        verbose_name = "partner logo"

    def __str__(self):
        return f"{self.company_name} logo"

    def clean(self):
        try:
            validate_and_convert_image(self.image)
        except ValidationError as e:
            raise ValidationError({"image": e})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class News(models.Model):
    image = models.FileField(upload_to="news/")
    date = models.DateField()
    title = models.CharField()
    description = models.TextField()
    link_to_news = models.URLField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "news"

    def __str__(self):
        return f"{self.title}"

    def clean(self):
        try:
            validate_and_convert_image(self.image)
        except ValidationError as e:
            raise ValidationError({"image": e})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Contacts(Singleton):
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    youtube_link = models.URLField()
    facebook_link = models.URLField()
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "contacts"

    def __str__(self):
        return "Contacts"


class PDFReport(Singleton):
    title = models.CharField(max_length=255)
    file_url = models.FileField(upload_to=UploadToPath("pdf-report/"))
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "PDF report"

    def __str__(self):
        return f"{self.title}"

    def clean(self):
        try:
            validate_pdf_file(self.file_url)
        except ValidationError as e:
            raise ValidationError({"file_url": e})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
