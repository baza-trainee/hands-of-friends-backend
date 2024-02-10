"""Help texts for the content management app models."""
from django.utils.translation import gettext_lazy as _

from validators.constants import MAX_FILE_SIZE

# General help texts
IMAGE_HELP_TEXT = _(
    f"Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg та не "
    f"перевищувати {int(MAX_FILE_SIZE / 1024 / 1024)} МБ."
)

PDF_HELP_TEXT = _(
    f"Файл має бути у форматі .pdf та не перевищувати {int(MAX_FILE_SIZE / 1024 / 1024)} МБ."
)
