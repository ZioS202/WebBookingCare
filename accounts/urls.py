from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signin/', views.user_signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.user_signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path(
        'change-password',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/changePasswordForm.html',
            success_url = '/accounts/signout'
        ),
        name='change_password'
    ),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = "accounts/password_reset_form.html"),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_done.html"),name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_confirm.html"),name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_complete.html"), name='password_reset_complete'),

]
