"""booking_care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from custom_MatorMarkdownEditor.views import markdown_uploader

urlpatterns = [
    path("doctor/", include("doctors.urls")),
    path("patient/", include("patients.urls")),
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("specialist/", include("specialists.urls")),
    path("clinic/", include("clinics.urls")),
    path("accounts/", include("accounts.urls")),
    path("bookings/", include("bookings.urls")),
    # path("notification/", include("notifications.urls")),
    # path("login/", LoginForm.as_view(), name="login"),
    # path("signup/", RegisterForm.as_view(), name="signup"),
    # path('logout/', LogoutForm.as_view(), name='logout'),
    path("martor/", include("martor.urls")),
    path("api/uploader/", markdown_uploader, name="markdown_uploader_page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
