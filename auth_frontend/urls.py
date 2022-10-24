from django.urls import path
from .views import LoginForm
from .views import RegisterForm

urlpatterns = [
    path("loginForm", LoginForm.as_view(), name="loginForm"),
    path("registerForm", RegisterForm.as_view(), name="registerForm"),
]