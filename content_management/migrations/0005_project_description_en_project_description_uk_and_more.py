# Generated by Django 5.0.1 on 2024-01-13 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0004_alter_project_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="description_uk",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="title_en",
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="title_uk",
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name="tender",
            name="description_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="tender",
            name="description_uk",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="tender",
            name="title_en",
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name="tender",
            name="title_uk",
            field=models.CharField(null=True),
        ),
    ]
