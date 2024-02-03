# Generated by Django 5.0.1 on 2024-01-30 18:34

import validators.feedback_form_validation
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FeedbackForm",
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
                    "name",
                    models.CharField(
                        max_length=50,
                        validators=[validators.feedback_form_validation.validate_name],
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        validators=[
                            validators.feedback_form_validation.validate_email_domain
                        ],
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=30,
                    ),
                ),
                ("message", models.TextField()),
                ("sent_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ("-sent_at",),
            },
        ),
    ]
