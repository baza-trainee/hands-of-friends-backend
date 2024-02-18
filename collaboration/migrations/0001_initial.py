# Generated by Django 5.0.1 on 2024-02-18 11:05

import validators.form_validation
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DonorForm",
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
                    "organization_name",
                    models.CharField(max_length=255, verbose_name="Organization Name"),
                ),
                (
                    "representative_name",
                    models.CharField(
                        max_length=50,
                        validators=[validators.form_validation.validate_name],
                        verbose_name="Representative Name",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        validators=[validators.form_validation.validate_email_domain],
                        verbose_name="Email",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=30,
                        validators=[validators.form_validation.validate_phone_number],
                        verbose_name="Phone",
                    ),
                ),
                ("message", models.TextField(max_length=300, verbose_name="Message")),
                (
                    "sent_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Sent at"),
                ),
            ],
            options={
                "verbose_name": "Partner form",
                "verbose_name_plural": "Partners forms",
                "ordering": ("-sent_at",),
            },
        ),
        migrations.CreateModel(
            name="PartnerForm",
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
                    "organization_name",
                    models.CharField(max_length=255, verbose_name="Organization Name"),
                ),
                (
                    "representative_name",
                    models.CharField(
                        max_length=50,
                        validators=[validators.form_validation.validate_name],
                        verbose_name="Representative Name",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        validators=[validators.form_validation.validate_email_domain],
                        verbose_name="Email",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=30,
                        validators=[validators.form_validation.validate_phone_number],
                        verbose_name="Phone",
                    ),
                ),
                ("message", models.TextField(max_length=300, verbose_name="Message")),
                (
                    "sent_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Sent at"),
                ),
            ],
            options={
                "verbose_name": "Partner form",
                "verbose_name_plural": "Partners forms",
                "ordering": ("-sent_at",),
            },
        ),
        migrations.CreateModel(
            name="VolunteerForm",
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
                        validators=[validators.form_validation.validate_name],
                        verbose_name="Name",
                    ),
                ),
                ("city", models.CharField(max_length=255, verbose_name="City")),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        validators=[validators.form_validation.validate_email_domain],
                        verbose_name="Email",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=30,
                        validators=[validators.form_validation.validate_phone_number],
                        verbose_name="Phone",
                    ),
                ),
                ("message", models.TextField(max_length=300, verbose_name="Message")),
                (
                    "sent_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Sent at"),
                ),
            ],
            options={
                "verbose_name": "Partner form",
                "verbose_name_plural": "Partners forms",
                "ordering": ("-sent_at",),
            },
        ),
    ]