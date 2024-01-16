# Generated by Django 5.0.1 on 2024-01-16 15:32

import content_management.upload_to_path
import content_management.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0006_alter_project_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeamMember",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to=content_management.upload_to_path.UploadToPath(
                            "team-members/"
                        ),
                        validators=[content_management.validators.validate_image],
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                ("full_name_uk", models.CharField(max_length=255, null=True)),
                ("full_name_en", models.CharField(max_length=255, null=True)),
                ("position", models.CharField(max_length=255)),
                ("position_uk", models.CharField(max_length=255, null=True)),
                ("position_en", models.CharField(max_length=255, null=True)),
                ("added_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "team member",
                "verbose_name_plural": "team members",
                "ordering": ["-added_at"],
            },
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(
                upload_to=content_management.upload_to_path.UploadToPath("projects/"),
                validators=[content_management.validators.validate_image],
            ),
        ),
    ]