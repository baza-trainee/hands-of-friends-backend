# Generated by Django 5.0.2 on 2024-03-03 10:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "content_management",
            "0043_alter_news_description_alter_news_description_en_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 500 символів.",
                max_length=600,
                verbose_name="Короткий Опис",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="description_en",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 500 символів.",
                max_length=600,
                null=True,
                verbose_name="Короткий Опис",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="description_uk",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 500 символів.",
                max_length=600,
                null=True,
                verbose_name="Короткий Опис",
            ),
        ),
    ]
