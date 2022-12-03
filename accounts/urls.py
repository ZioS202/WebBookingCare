from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/', views.profile, name='profile')
]
