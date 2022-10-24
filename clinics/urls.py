from django.urls import path
from .views import ClinicDetail

urlpatterns = [path("clinicDetail", ClinicDetail.as_view(), name="clinicDetail")]
