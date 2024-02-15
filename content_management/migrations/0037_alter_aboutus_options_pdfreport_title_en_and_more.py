# Generated by Django 5.0.1 on 2024-02-15 15:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0036_aboutus_alter_heroslider_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="aboutus",
            options={"verbose_name": "Про нас", "verbose_name_plural": "Про нас"},
        ),
        migrations.AddField(
            model_name="pdfreport",
            name="title_en",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                null=True,
                verbose_name="Назва",
            ),
        ),
        migrations.AddField(
            model_name="pdfreport",
            name="title_uk",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                null=True,
                verbose_name="Назва",
            ),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="principles",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 2500 символів.",
                max_length=2500,
                verbose_name="Приципи",
            ),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="principles_en",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 2500 символів.",
                max_length=2500,
                null=True,
                verbose_name="Приципи",
            ),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="principles_uk",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 2500 символів.",
                max_length=2500,
                null=True,
                verbose_name="Приципи",
            ),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="values",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 2500 символів.",
                max_length=2500,
                verbose_name="Цінності",
            ),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="values_en",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 2500 символів.",
                max_length=2500,
                null=True,
                verbose_name="Цінності",
            ),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="values_uk",
            field=ckeditor.fields.RichTextField(
                help_text="Максимальна довжина тексту: 2500 символів.",
                max_length=2500,
                null=True,
                verbose_name="Цінності",
            ),
        ),
        migrations.AlterField(
            model_name="heroslider",
            name="alt_text",
            field=models.CharField(
                blank=True,
                help_text="Альтернативний текст для зображення, що описує зображення для SEO. Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Альтернативний Текст Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="heroslider",
            name="alt_text_en",
            field=models.CharField(
                blank=True,
                help_text="Альтернативний текст для зображення, що описує зображення для SEO. Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Альтернативний Текст Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="heroslider",
            name="alt_text_uk",
            field=models.CharField(
                blank=True,
                help_text="Альтернативний текст для зображення, що описує зображення для SEO. Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Альтернативний Текст Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="link_to_news",
            field=models.URLField(verbose_name="Link to News"),
        ),
    ]