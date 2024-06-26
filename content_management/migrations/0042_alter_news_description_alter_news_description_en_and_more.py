# Generated by Django 5.0.1 on 2024-02-24 08:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0041_alter_project_end_date_alter_tender_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="description",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 1000 символів.",
                max_length=1600,
                verbose_name="Опис",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="description_en",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 1000 символів.",
                max_length=1600,
                null=True,
                verbose_name="Опис",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="description_uk",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 1000 символів.",
                max_length=1600,
                null=True,
                verbose_name="Опис",
            ),
        ),
    ]
