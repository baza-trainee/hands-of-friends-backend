# Generated by Django 5.0.1 on 2024-02-10 14:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="feedbackform",
            options={
                "ordering": ("-sent_at",),
                "verbose_name": "Feedback form",
                "verbose_name_plural": "Feedback forms",
            },
        ),
    ]
