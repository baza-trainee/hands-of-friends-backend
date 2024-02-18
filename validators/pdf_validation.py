"""Validator for PDF files."""

from django.core.exceptions import ValidationError
from django.db.models.fields.files import FieldFile
from django.utils.translation import gettext as _

from validators.constants import MAX_FILE_SIZE
from validators.file_utils import FileUtility


def is_pdf(file_name: str) -> bool:
    """Check if a file has a PDF extension."""
    return file_name.lower().endswith(".pdf")


def validate_pdf_file(file_field: FieldFile) -> None:
    """Validate that a file is a PDF and its size is within the limit."""
    if not is_pdf(file_field.name):
        raise ValidationError(
            "Непідтримуваний розширення файлу. Дозволене розширення: pdf."
        )

    file_size = FileUtility.get_file_size(file_field)
    if file_size > MAX_FILE_SIZE:
        raise ValidationError(
            f"Розмір PDF занадто великий. Максимальний розмір: {MAX_FILE_SIZE / 1024 / 1024} MB."
        )
