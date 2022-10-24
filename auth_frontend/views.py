from django.views.generic import TemplateView

# Create your views here.


class LoginForm(TemplateView):
    template_name = "auth_frontend/loginForm.html"

class RegisterForm(TemplateView):
    template_name = "auth_frontend/registerForm.html"
