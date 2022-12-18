from django.urls import path
from .views import DoctorDetail
from . import views

urlpatterns = [
    path("", views.indexDoctor, name="index"),
    path("findDoctor/", views.findDoctor, name="findDoctor"),
    path("doctorDetail/<int:pk>", DoctorDetail.as_view(), name="doctorDetail"),
]
