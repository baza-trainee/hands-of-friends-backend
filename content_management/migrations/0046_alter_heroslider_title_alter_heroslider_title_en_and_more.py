# Generated by Django 5.0.2 on 2024-03-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0045_alter_tender_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="heroslider",
            name="title",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 120 символів.",
                max_length=120,
                verbose_name="Назва",
            ),
        ),
        migrations.AlterField(
            model_name="heroslider",
            name="title_en",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 120 символів.",
                max_length=120,
                null=True,
                verbose_name="Назва",
            ),
        ),
        migrations.AlterField(
            model_name="heroslider",
            name="title_uk",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 120 символів.",
                max_length=120,
                null=True,
                verbose_name="Назва",
            ),
        ),
    ]
