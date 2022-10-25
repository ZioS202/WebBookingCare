from django.urls import path
from .views import LoginForm
from .views import RegisterForm

urlpatterns = [
    path("login/", LoginForm.as_view(), name="login"),
    path("signup/", RegisterForm.as_view(), name="signup"),
]
