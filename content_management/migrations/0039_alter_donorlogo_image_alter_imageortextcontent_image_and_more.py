# Generated by Django 5.0.1 on 2024-02-16 18:21

import ckeditor.fields
import content_management.upload_to_path
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0038_alter_pdfreport_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donorlogo",
            name="image",
            field=models.FileField(
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg. Після завантаження зображення буде автоматично компресоване до 2 МБ та змінено на формат .webp.",
                upload_to=content_management.upload_to_path.UploadToPath(
                    "donors-logos/"
                ),
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="imageortextcontent",
            name="image",
            field=models.FileField(
                blank=True,
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg. Після завантаження зображення буде автоматично компресоване до 2 МБ та змінено на формат .webp.",
                null=True,
                upload_to=content_management.upload_to_path.UploadToPath(
                    "project_contents/"
                ),
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="description",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 1000 символів.",
                max_length=1000,
                verbose_name="Опис",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="description_en",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 1000 символів.",
                max_length=1000,
                null=True,
                verbose_name="Опис",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="description_uk",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 1000 символів.",
                max_length=1000,
                null=True,
                verbose_name="Опис",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="image",
            field=models.FileField(
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg. Після завантаження зображення буде автоматично компресоване до 2 МБ та змінено на формат .webp.",
                upload_to=content_management.upload_to_path.UploadToPath("news/"),
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="partnerlogo",
            name="image",
            field=models.FileField(
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg. Після завантаження зображення буде автоматично компресоване до 2 МБ та змінено на формат .webp.",
                upload_to=content_management.upload_to_path.UploadToPath(
                    "partner-logos/"
                ),
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FileField(
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg. Після завантаження зображення буде автоматично компресоване до 2 МБ та змінено на формат .webp.",
                upload_to=content_management.upload_to_path.UploadToPath("projects/"),
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="image",
            field=models.FileField(
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg. Після завантаження зображення буде автоматично компресоване до 2 МБ та змінено на формат .webp.",
                upload_to=content_management.upload_to_path.UploadToPath(
                    "team-members/"
                ),
                verbose_name="Зображення",
            ),
        ),
    ]