from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class CustomPasswordResetView(auth_views.PasswordResetView):
    success_url = reverse_lazy("user:password_reset_done")


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy("user:password_reset_complete")
