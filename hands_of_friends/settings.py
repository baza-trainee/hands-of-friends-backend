"""
Django settings for hands_of_friends project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

import certifi
from django.utils.translation import gettext_lazy as _

from dotenv import load_dotenv

# Loading env variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "") == "True"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,0.0.0.0").split(",")

# CORS
default_origins = "http://localhost:8000"

CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get("CORS_ALLOWED_ORIGINS", default_origins).split(",")
    if origin.strip()
]

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get("CSRF_TRUSTED_ORIGINS", default_origins).split(",")
    if origin.strip()
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Adding Render hostname to allowed hosts
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    "modeltranslation",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    "ckeditor",
    "import_export",
    "user",
    "content_management",
    "feedback.apps.FeedbackConfig",
    "collaboration.apps.CollaborationConfig",
    "email_config",
    "django_cleanup.apps.CleanupConfig",  # Must be the last one in the list
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "configurations.middleware.admin_middleware.ForceAdminLanguageMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hands_of_friends.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hands_of_friends.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ["POSTGRES_HOST"],
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "user.User"

LOGIN_URL = "admin:login"
LOGIN_REDIRECT_URL = "/admin/"

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGES = (
    ("uk", _("Ukrainian")),
    ("en", _("English")),
)

LANGUAGE_CODE = "uk"
MODELTRANSLATION_DEFAULT_LANGUAGE = "uk"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Locale
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_STORAGE = (
    "configurations.storage_backends.ForgivingCompressedManifestStaticFilesStorage"
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = os.getenv("MEDIA_URL", "/media/")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Hands of Friends Website API",
    "DESCRIPTION": "Endpoint for dynamic content of Hands of Friends website.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "defaultModelRendering": "model",
        "defaultModelsExpandDepth": 2,
        "defaultModelExpandDepth": 2,
    },
}

EMAIL_BACKEND = "email_config.backends.CustomEmailBackend"

# SSL
os.environ["SSL_CERT_FILE"] = certifi.where()

# CKEditor
CKEDITOR_CONFIGS = {
    "default": {
        "skin": "moono",
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
        "toolbar_CustomToolbarConfig": [
            {"name": "document", "items": ["Source", "-", "Save"]},
            {
                "name": "clipboard",
                "items": [
                    "Cut",
                    "Copy",
                    "Paste",
                    "PasteText",
                    "PasteFromWord",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                    "-",
                    "RemoveFormat",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "Blockquote",
                    "CreateDiv",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink"]},
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {"name": "tools", "items": ["Maximize", "ShowBlocks"]},
        ],
        "toolbar": "CustomToolbarConfig",
        "height": 291,
        "width": "100%",
        "filebrowserWindowWidth": "100%",
        "extraPlugins": ",".join(
            [
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
            ]
        ),
    }
}

# Jazzmin Configuration (Admin Panel)
JAZZMIN_SETTINGS = {
    "site_title": "Руки Друзів",
    "site_header": "Руки Друзів",
    "site_brand": "Руки Друзів",
    "site_title_short": "РД",
    "site_footer": "Руки Друзів",
    "site_logo": "images/logo_white.png",
    "login_logo": "images/logo.svg",
    "site_logo_classes": "img-circle",
    "welcome_sign": "Ласкаво просимо до панелі адміністрування сайту Руки Друзів",
    "language_chooser": False,
    "default_icon_parents": "fas fa-caret-right",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": True,
    "brand_small_text": True,
    "brand_colour": "navbar-dark",
    "accent": "accent-lightblue",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-lightblue",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-outline-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
