# Generated by Django 5.0.1 on 2024-01-13 20:44

import content_management.upload_to_path
import content_management.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0003_project_alter_tender_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(
                upload_to=content_management.upload_to_path.UploadToPath(
                    "project-images/"
                ),
                validators=[content_management.validators.validate_image],
            ),
        ),
    ]