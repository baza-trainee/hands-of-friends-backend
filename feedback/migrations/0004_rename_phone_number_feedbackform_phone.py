# Generated by Django 5.0.1 on 2024-02-29 18:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "feedback",
            "0003_alter_feedbackform_email_alter_feedbackform_message_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="feedbackform",
            old_name="phone_number",
            new_name="phone",
        ),
    ]