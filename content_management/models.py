from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _

from content_management.upload_to_path import UploadToPath
from validators.image_validation import validate_and_convert_image
from validators.pdf_validation import validate_pdf_file
from ckeditor.fields import RichTextField


class Singleton(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise Exception(
                _(f"Only one {self.__class__.__name__} instance is allowed.")
            )
        super().save(*args, **kwargs)


class Tender(models.Model):
    title = models.CharField(verbose_name=_("Title"))
    description = RichTextField(verbose_name=_("Description"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        ordering = ["-is_active", "-start_date"]
        verbose_name = _("Tender")
        verbose_name_plural = _("Tenders")

    def __str__(self):
        return f"{self.title} ({self.start_date} - {self.end_date})"

    def clean(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError(_("Start date cannot be after end date."))


class Project(models.Model):
    image = models.FileField(upload_to="projects/", verbose_name=_("Image"))
    title = models.CharField(verbose_name=_("Title"))
    description = RichTextField(verbose_name=_("Description"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        ordering = ["-is_active", "-created_at"]
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

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
    image = models.FileField(upload_to="team-members/", verbose_name=_("Image"))
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    position = models.CharField(max_length=255, verbose_name=_("Position"))
    added_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Added At"))

    class Meta:
        ordering = ["-added_at"]
        verbose_name = _("Team member")
        verbose_name_plural = _("Team members")

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
    image = models.FileField(upload_to="partner-logos/", verbose_name=_("Image"))
    company_name = models.CharField(
        unique=True, null=True, blank=True, verbose_name=_("Company Name")
    )
    added_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Added At"))

    class Meta:
        ordering = ["company_name"]
        verbose_name = _("Partner logo")
        verbose_name_plural = _("Partner logos")

    def __str__(self):
        return _(f"{self.company_name} logo")

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
    image = models.FileField(upload_to="news/", verbose_name=_("Image"))
    date = models.DateField(verbose_name=_("Date"))
    title = models.CharField(verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    link_to_news = models.URLField(verbose_name=_("Link to News"))
    added_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Added At"))

    class Meta:
        ordering = ["-date"]
        verbose_name = _("News")
        verbose_name_plural = _("News")

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
    phone_number = models.CharField(max_length=255, verbose_name=_("Phone Number"))
    email = models.EmailField(verbose_name=_("Email"))
    youtube_link = models.URLField(verbose_name=_("Youtube Link"))
    facebook_link = models.URLField(verbose_name=_("Facebook Link"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return _("Contacts")


class PDFReport(Singleton):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    file_url = models.FileField(
        upload_to=UploadToPath("pdf-report/"), verbose_name=_("File URL")
    )
    added_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Added At"))

    class Meta:
        verbose_name = _("PDF report")
        verbose_name_plural = _("PDF reports")

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
