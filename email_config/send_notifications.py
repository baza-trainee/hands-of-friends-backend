from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import formats

from collaboration.models import PartnerForm, DonorForm, VolunteerForm
from feedback.models import FeedbackForm as Feedback
from email_config.models import Recipient
from email_config.utils import send_email


@receiver(post_save, sender=PartnerForm)
def send_partner_form_email(sender, instance, created, **kwargs):
    if created:
        formatted_sent_at = formats.date_format(instance.sent_at, "DATETIME_FORMAT")
        subject = f"Нова відповідь з форми Партнери: {instance.organization_name}"
        message = (
            f"Деталі:\n"
            f"Організація: {instance.organization_name}\n"
            f"Імʼя: {instance.representative_name}\n"
            f"Email: {instance.email}\n"
            f"Телефон: {instance.phone}\n"
            f"Повідомлення: {instance.message}\n"
            f"Форму відправлено: {formatted_sent_at}"
        )
        recipient_emails = [recipient.email for recipient in Recipient.objects.all()]
        send_email(subject, message, recipient_emails)


@receiver(post_save, sender=DonorForm)
def send_donor_form_email(sender, instance, created, **kwargs):
    if created:
        formatted_sent_at = formats.date_format(instance.sent_at, "DATETIME_FORMAT")
        subject = f"Нова відповідь з форми Донори: {instance.organization_name}"
        message = (
            f"Деталі:\n"
            f"Організація: {instance.organization_name}\n"
            f"Імʼя: {instance.representative_name}\n"
            f"Email: {instance.email}\n"
            f"Телефон: {instance.phone}\n"
            f"Повідомлення: {instance.message}\n"
            f"Форму відправлено: {formatted_sent_at}"
        )
        recipient_emails = [recipient.email for recipient in Recipient.objects.all()]
        send_email(subject, message, recipient_emails)


@receiver(post_save, sender=VolunteerForm)
def send_volunteer_form_email(sender, instance, created, **kwargs):
    if created:
        formatted_sent_at = formats.date_format(instance.sent_at, "DATETIME_FORMAT")
        subject = f"Нова відповідь з форми Волонтери: {instance.name}"
        message = (
            f"Деталі:\n"
            f"Імʼя: {instance.name}\n"
            f"Email: {instance.email}\n"
            f"Телефон: {instance.phone}\n"
            f"Повідомлення: {instance.message}\n"
            f"Форму відправлено: {formatted_sent_at}"
        )
        recipient_emails = [recipient.email for recipient in Recipient.objects.all()]
        send_email(subject, message, recipient_emails)


@receiver(post_save, sender=Feedback)
def send_feedback_email(sender, instance, created, **kwargs):
    if created:
        formatted_sent_at = formats.date_format(instance.sent_at, "DATETIME_FORMAT")
        subject = f"Новий відгук від {instance.name}"
        message = (
            f"Деталі:\n"
            f"Імʼя: {instance.name}\n"
            f"Email: {instance.email}\n"
            f"Телефон: {instance.phone_number}\n"
            f"Повідомлення: {instance.message}\n"
            f"Форму відправлено: {formatted_sent_at}"
        )
        recipient_emails = [recipient.email for recipient in Recipient.objects.all()]
        send_email(subject, message, recipient_emails)
