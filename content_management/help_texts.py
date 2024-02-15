"""Help texts for the content management app models."""
from django.utils.translation import gettext_lazy as _

from validators.constants import MAX_FILE_SIZE

# General help texts
IMAGE_HELP_TEXT = _(
    f"Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg та не перевищувати {int(MAX_FILE_SIZE / 1024 / 1024)} МБ. "
    f"Після завантаження зображення буде автоматично компресоване та змінено на формат .webp."
)

IMAGE_HELP_TEXT_NO_COMPRESSION = _(
    f"Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg та не перевищувати {int(MAX_FILE_SIZE / 1024 / 1024)} МБ."
)

ALT_TEXT_HELP_TEXT = _(
    "Альтернативний текст для зображення, що описує зображення для SEO. Максимальна довжина тексту: 100 символів."
)

PDF_HELP_TEXT = _(
    f"Файл має бути у форматі .pdf та не перевищувати {int(MAX_FILE_SIZE / 1024 / 1024)} МБ."
)

TEXT_LENGTH_HELP_TEXT_100 = _("Максимальна довжина тексту: 100 символів.")
TEXT_LENGTH_HELP_TEXT_200 = _("Максимальна довжина тексту: 200 символів.")
TEXT_LENGTH_HELP_TEXT_500 = _("Максимальна довжина тексту: 500 символів.")
TEXT_LENGTH_HELP_TEXT_2500 = _("Максимальна довжина тексту: 2500 символів.")
IS_SHOWN_HELP_TEXT = _("Позначте, якщо ви хочете, щоб цей об'єкт був видимим на сайті.")
