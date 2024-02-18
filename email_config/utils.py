from django.core.mail import get_connection, EmailMessage
from email_config.models import EmailSettings


def send_email(subject, message, recipient_list):
    settings = EmailSettings.objects.first()
    if settings:
        connection = get_connection(
            backend=settings.backend,
            host=settings.host,
            port=settings.port,
            username=settings.host_user,
            password=settings.host_password,
            use_tls=settings.use_tls,
            use_ssl=settings.use_ssl,
        )
        email = EmailMessage(subject, message, to=recipient_list, connection=connection)
        email.send()
