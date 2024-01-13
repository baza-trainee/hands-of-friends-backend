"""Image and file validators for content_management app."""

from django.core.exceptions import ValidationError
from PIL import Image

MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB
VALID_IMAGE_EXTENSIONS = ["jpg", "jpeg", "webp", "png", "svg"]


def validate_image(value: Image) -> None:
    """Validator for image files."""

    try:
        img = Image.open(value)
    except Exception:
        raise ValidationError("Invalid image format.")

    if value.size > MAX_FILE_SIZE:
        raise ValidationError("Image size exceeds 2 MB.")

    file_extension = value.name.split(".")[-1].lower()

    if file_extension not in VALID_IMAGE_EXTENSIONS:
        raise ValidationError(
            "Unsupported file extension. Allowed extensions are jpg, jpeg, webp, png, svg."
        )
