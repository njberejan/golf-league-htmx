
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
    LogoutView, PasswordResetDoneView, PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView
)

from main.views import LoginPageView, UserCreationPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginPageView.as_view(template_name="main/login.html"), name="login"),
    path('register/', UserCreationPageView.as_view(), name="user_creation"),
    path('reset_password/', PasswordResetView.as_view(), name="reset_password"),
    path('reset-password_sent/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('main/', include("main.urls")),
]
