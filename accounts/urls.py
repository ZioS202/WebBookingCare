from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    # path("login/", LoginForm.as_view(), name="login"),
    #path("signup/", RegisterForm.as_view(), name="signup"),
    path('signup/', views.signup, name='signup'),
]
