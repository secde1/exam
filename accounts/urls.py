from django.urls import path
from django.contrib.auth.views import( # noqa
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from accounts.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path(
        'reset-password',
        PasswordResetView.as_view(template_name='password_reset.html'),
        name='reset_password'),

    path(
        'reset-password-dane',
        PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),

    path(
        'reset-password/<uidb64>/<token>',
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),

    path(
        'reset-password-complete',
        PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
]
