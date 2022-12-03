from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signin/', views.user_signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.user_signout, name='signout'),
    path('profile/', views.profile, name='profile')
]
