from django.core.mail.backends.smtp import EmailBackend as SMTPEmailBackend
from .models import EmailSettings


class CustomEmailBackend(SMTPEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently, **kwargs)
        settings = EmailSettings.objects.first()
        if settings:
            self.host = settings.host
            self.port = settings.port
            self.username = settings.host_user
            self.password = settings.host_password
            self.use_tls = settings.use_tls
            self.use_ssl = settings.use_ssl
        else:
            raise ValueError("No EmailSettings configured.")
