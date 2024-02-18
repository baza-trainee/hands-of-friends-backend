from django.contrib.auth import views as auth_views
from django.urls import path

from user.views import CustomPasswordResetView, CustomPasswordResetConfirmView

urlpatterns = [
    path(
        "password_reset/",
        CustomPasswordResetView.as_view(),
        name="admin_password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]

app_name = "user"
