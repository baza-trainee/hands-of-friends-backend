from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _

from content_management.upload_to_path import UploadToPath

from validators.image_validation import (
    validate_and_convert_image,
    validate_image_size,
    is_valid_image_extension,
)
from validators.pdf_validation import validate_pdf_file

from content_management.help_texts import (
    IMAGE_HELP_TEXT,
    PDF_HELP_TEXT,
    TEXT_LENGTH_HELP_TEXT_100,
    TEXT_LENGTH_HELP_TEXT_200,
    TEXT_LENGTH_HELP_TEXT_500,
    IS_SHOWN_HELP_TEXT,
    IMAGE_HELP_TEXT_NO_COMPRESSION,
    ALT_TEXT_HELP_TEXT,
    TEXT_LENGTH_HELP_TEXT_2500,
)
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
    title = models.CharField(
        max_length=200, verbose_name=_("Title"), help_text=TEXT_LENGTH_HELP_TEXT_200
    )
    description = RichTextField(verbose_name=_("Description"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    is_shown = models.BooleanField(
        default=True, verbose_name=_("Is Shown"), help_text=IS_SHOWN_HELP_TEXT
    )
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
    image = models.FileField(
        upload_to=UploadToPath("projects/"),
        verbose_name=_("Image"),
        help_text=IMAGE_HELP_TEXT,
    )
    title = models.CharField(
        max_length=200, verbose_name=_("Title"), help_text=TEXT_LENGTH_HELP_TEXT_200
    )
    description = RichTextField(
        max_length=500,
        verbose_name=_("Short Description"),
        help_text=TEXT_LENGTH_HELP_TEXT_500,
    )
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    is_shown = models.BooleanField(
        default=True, verbose_name=_("Is Shown"), help_text=IS_SHOWN_HELP_TEXT
    )
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


class ImageOrTextContent(models.Model):
    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="content",
        verbose_name=_("Project"),
    )
    image = models.FileField(
        upload_to=UploadToPath("project_contents/"),
        verbose_name=_("Image"),
        help_text=IMAGE_HELP_TEXT,
        blank=True,
        null=True,
    )
    text = RichTextField(
        blank=True,
        null=True,
        verbose_name=_("Text"),
        help_text=_("Enter text for the content."),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Project Content")
        verbose_name_plural = _("Project Contents")

    def __str__(self):
        return _(f"Content for {self.project.title}")

    def clean(self):
        if not self.image and not self.text:
            raise ValidationError(_("Please provide either an image or text."))
        if self.image:
            try:
                validate_and_convert_image(self.image)
            except ValidationError as e:
                raise ValidationError({"image": e})
        super().clean()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class TeamMember(models.Model):
    image = models.FileField(
        upload_to=UploadToPath("team-members/"),
        verbose_name=_("Image"),
        help_text=IMAGE_HELP_TEXT,
    )
    full_name = models.CharField(
        max_length=200, verbose_name=_("Full Name"), help_text=TEXT_LENGTH_HELP_TEXT_200
    )
    position = models.CharField(
        max_length=200, verbose_name=_("Position"), help_text=TEXT_LENGTH_HELP_TEXT_200
    )
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
        super().save(*args, **kwargs)


class PartnerLogo(models.Model):
    image = models.FileField(
        upload_to=UploadToPath("partner-logos/"),
        verbose_name=_("Image"),
        help_text=IMAGE_HELP_TEXT,
    )
    company_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Company Name"),
        help_text=TEXT_LENGTH_HELP_TEXT_100,
    )
    added_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Added At"))

    class Meta:
        ordering = ["company_name"]
        verbose_name = _("Partner logo")
        verbose_name_plural = _("Partner logos")

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


class DonorLogo(models.Model):
    image = models.FileField(
        upload_to=UploadToPath("donors-logos/"),
        verbose_name=_("Image"),
        help_text=IMAGE_HELP_TEXT,
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Donor Name"),
        help_text=TEXT_LENGTH_HELP_TEXT_100,
    )
    added_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Added At"))

    class Meta:
        ordering = ["name"]
        verbose_name = _("Donor logo")
        verbose_name_plural = _("Donor logos")

    def __str__(self):
        return f"{self.name} logo"

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
    image = models.FileField(
        upload_to=UploadToPath("news/"),
        verbose_name=_("Image"),
        help_text=IMAGE_HELP_TEXT,
    )
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


class PDFReport(models.Model):
    title = models.CharField(
        max_length=200, verbose_name=_("Title"), help_text=TEXT_LENGTH_HELP_TEXT_200
    )
    file_url = models.FileField(
        upload_to=UploadToPath("pdf-report/"),
        verbose_name=_("File URL"),
        help_text=PDF_HELP_TEXT,
    )
    added_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Added At"))

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")

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


class HeroSlider(models.Model):
    title = models.CharField(
        max_length=200, verbose_name=_("Title"), help_text=TEXT_LENGTH_HELP_TEXT_200
    )
    image = models.FileField(
        upload_to=UploadToPath("hero-slider/"),
        verbose_name=_("Image"),
        help_text=IMAGE_HELP_TEXT_NO_COMPRESSION,
    )
    alt_text = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Alt Text"),
        help_text=ALT_TEXT_HELP_TEXT,
    )

    class Meta:
        verbose_name = _("Hero Slider")
        verbose_name_plural = _("Hero Sliders")

    def __str__(self):
        return f"{self.title}"

    def clean(self):
        try:
            is_valid_image_extension(self.image.name)
            validate_image_size(self.image)
        except ValidationError as e:
            raise ValidationError({"image": e})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class AboutUs(Singleton):
    history = RichTextField(
        max_length=2500, verbose_name=_("History"), help_text=TEXT_LENGTH_HELP_TEXT_2500
    )
    principles = RichTextField(
        max_length=2500,
        verbose_name=_("Principles"),
        help_text=TEXT_LENGTH_HELP_TEXT_2500,
    )
    values = RichTextField(
        max_length=2500, verbose_name=_("Values"), help_text=TEXT_LENGTH_HELP_TEXT_2500
    )

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")

    def __str__(self):
        return _("About Us")
