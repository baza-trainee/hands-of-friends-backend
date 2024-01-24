"""Image and file validators for content_management app."""
import io
import os

from django.core.exceptions import ValidationError
from PIL import Image
from django.db.models.fields.files import FileField
from django.core.files.uploadedfile import InMemoryUploadedFile

MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB
VALID_IMAGE_EXTENSIONS = ["jpg", "jpeg", "webp", "png", "svg"]


def check_image_file_extension(image_field: Image) -> None:
    if not image_field.name.lower().endswith(tuple(VALID_IMAGE_EXTENSIONS)):
        raise ValidationError(
            "Unsupported file extension. Allowed extensions are jpg, jpeg, webp, png, svg."
        )


def convert_and_optimize_webp(image_field: Image) -> None:
    try:
        img = Image.open(image_field)
    except IOError:
        raise ValidationError("Invalid image file.")

    output_io_stream = io.BytesIO()
    quality = 90
    img.save(output_io_stream, format="WEBP", quality=quality)
    output_io_stream.seek(0)

    while output_io_stream.getbuffer().nbytes > MAX_FILE_SIZE and quality > 10:
        quality -= 10
        output_io_stream = io.BytesIO()
        img.save(output_io_stream, format="WEBP", quality=quality)
        output_io_stream.seek(0)

    file_name = image_field.name.split(".")[0] + ".webp"
    image_field.file = InMemoryUploadedFile(
        output_io_stream,
        "ImageField",
        file_name,
        "image/webp",
        output_io_stream.getbuffer().nbytes,
        None,
    )
    image_field.name = file_name


def validate_image(image_field: Image) -> None:
    """Validator for image files."""

    check_image_file_extension(image_field)

    file_extension = image_field.name.split(".")[-1].lower()
    if file_extension in ["svg"]:
        return

    try:
        img = Image.open(image_field)
        convert_and_optimize_webp(image_field)
    except Exception:
        raise ValidationError("Invalid image format.")


def check_if_pdf_file(file_field: FileField) -> None:
    if not file_field.name.lower().endswith(".pdf"):
        raise ValidationError("Unsupported file extension. Allowed extension is pdf.")


def validate_pdf_file(file_field: FileField) -> None:
    """Validator for PDF files."""
    check_if_pdf_file(file_field)

    if os.path.getsize(file_field.path) > MAX_FILE_SIZE:
        raise ValidationError(
            "PDF size is too large even after compression. Max size is 2 MB."
        )
