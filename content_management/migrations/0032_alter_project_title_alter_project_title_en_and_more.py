# Generated by Django 5.0.1 on 2024-02-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "content_management",
            "0031_alter_donorlogo_image_alter_imageortextcontent_image_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                verbose_name="Назва",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title_en",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                null=True,
                verbose_name="Назва",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title_uk",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                null=True,
                verbose_name="Назва",
            ),
        ),
    ]
