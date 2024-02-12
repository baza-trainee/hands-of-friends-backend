# Generated by Django 5.0.1 on 2024-02-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "content_management",
            "0023_alter_pdfreport_options_alter_donorlogo_image_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="tender",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Назва"),
        ),
        migrations.AlterField(
            model_name="tender",
            name="title_en",
            field=models.CharField(max_length=200, null=True, verbose_name="Назва"),
        ),
        migrations.AlterField(
            model_name="tender",
            name="title_uk",
            field=models.CharField(max_length=200, null=True, verbose_name="Назва"),
        ),
    ]
