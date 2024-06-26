# Generated by Django 5.0.2 on 2024-03-09 14:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0044_alter_project_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tender",
            name="end_date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Дата завершення"
            ),
            preserve_default=False,
        ),
    ]
