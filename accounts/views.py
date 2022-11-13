from django.views.generic import TemplateView

# Create your views here.


class LoginForm(TemplateView):
    template_name = "accounts/loginForm.html"


class RegisterForm(TemplateView):
    template_name = "accounts/registerForm.html"
