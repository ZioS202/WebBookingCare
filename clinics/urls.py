from django.urls import path
from .views import ClinicDetail
from .views import FindClinic

urlpatterns = [
    path("clinicDetail/", ClinicDetail.as_view(), name="clinicDetail"),
    path("findClinic/", FindClinic.as_view(), name="findClinic"),
]
