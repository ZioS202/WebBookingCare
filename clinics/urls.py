from django.urls import path
from .views import ClinicDetail
from . import views

urlpatterns = [
    path("findClinic/", views.list_clinics, name="findClinic"),
    path("clinicDetail/<int:pk>", ClinicDetail.as_view(), name="clinicDetail"),
]
