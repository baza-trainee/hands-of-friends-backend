# Generated by Django 5.0.1 on 2024-02-17 10:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "content_management",
            "0039_alter_donorlogo_image_alter_imageortextcontent_image_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="partnerlogo",
            options={
                "ordering": ["name"],
                "verbose_name": "Логотип партнера",
                "verbose_name_plural": "Логотипи партнерів",
            },
        ),
        migrations.RenameField(
            model_name="partnerlogo",
            old_name="company_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="partnerlogo",
            old_name="company_name_en",
            new_name="name_en",
        ),
        migrations.RenameField(
            model_name="partnerlogo",
            old_name="company_name_uk",
            new_name="name_uk",
        ),
    ]
