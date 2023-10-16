from django.urls import path

from accounts.views import SinginView, RegisterView, LogoutView

urlpatterns = [
    path('login', SinginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', SinginView.as_view(), name='logout')
]