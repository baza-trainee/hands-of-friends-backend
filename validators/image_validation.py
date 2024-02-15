import io
from typing import Tuple

from django.core.exceptions import ValidationError
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.fields.files import FieldFile
from django.utils.translation import gettext as _

from validators.constants import VALID_IMAGE_EXTENSIONS, MAX_FILE_SIZE
from validators.file_utils import FileUtility


def is_valid_image_extension(file_name: str) -> None:
    """Check if the file has a valid image extension."""
    if not file_name.lower().endswith(tuple(VALID_IMAGE_EXTENSIONS)):
        raise ValidationError(
            "Непідтримуваний розширення файлу. Дозволені розширення: jpg, jpeg, webp, png, svg."
        )


def convert_image_to_webp(image: Image, quality: int = 90) -> Tuple[io.BytesIO, str]:
    """Convert the image to WEBP format with the specified quality."""
    output_io_stream = io.BytesIO()
    image.save(output_io_stream, format="WEBP", quality=quality)
    output_io_stream.seek(0)
    return output_io_stream, "image.webp"


def optimize_webp_size(image_stream: io.BytesIO, quality: int = 90) -> io.BytesIO:
    """Optimize the size of a WEBP image."""
    while image_stream.getbuffer().nbytes > MAX_FILE_SIZE and quality > 10:
        quality -= 10
        image_stream, _ = convert_image_to_webp(
            Image.open(image_stream), quality=quality
        )
    return image_stream


def validate_image_size(image_field: FieldFile) -> None:
    """Validate the image size."""
    file_size = FileUtility.get_file_size(image_field)
    if file_size > MAX_FILE_SIZE:
        raise ValidationError(
            f"Розмір зображення занадто великий. Максимальний розмір: {MAX_FILE_SIZE / 1024 / 1024} МБ."
        )


def validate_and_convert_image(image_field: FieldFile) -> None:
    """Validate and convert the image to WEBP format if necessary."""
    file_name = image_field.name

    is_valid_image_extension(file_name)

    file_extension = FileUtility.get_file_extension(file_name)

    if file_extension in ["svg", "webp"]:
        return

    try:
        img = Image.open(image_field)
        image_stream, file_name = convert_image_to_webp(img)
        image_stream = optimize_webp_size(image_stream)
        image_field.file = InMemoryUploadedFile(
            image_stream,
            "ImageField",
            file_name,
            "image/webp",
            image_stream.getbuffer().nbytes,
            None,
        )
        image_field.name = file_name

        validate_image_size(image_field)

    except Exception:
        raise ValidationError(
            "Недійсний формат зображення. Дозволені формати: jpg, jpeg, webp, png, svg."
        )
