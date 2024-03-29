# Generated by Django 5.0.1 on 2024-02-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0034_heroslider_alter_pdfreport_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="heroslider",
            options={
                "verbose_name": "Cлайдер для головної сторінки",
                "verbose_name_plural": "Cлайдери для головної сторінки",
            },
        ),
        migrations.AddField(
            model_name="heroslider",
            name="alt_text_en",
            field=models.CharField(
                blank=True,
                help_text="Альтернативний текст для зображення, що описує зображення для SEO. Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Alt Text",
            ),
        ),
        migrations.AddField(
            model_name="heroslider",
            name="alt_text_uk",
            field=models.CharField(
                blank=True,
                help_text="Альтернативний текст для зображення, що описує зображення для SEO. Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Alt Text",
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
                verbose_name="Alt Text",
            ),
        ),
    ]
