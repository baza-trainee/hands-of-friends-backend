# Generated by Django 5.0.1 on 2024-01-11 15:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tender",
            old_name="main_text",
            new_name="description",
        ),
    ]
