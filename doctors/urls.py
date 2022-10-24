from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexDoctor, name="index"),
    path("manageClinic/", views.manageClinic, name="manageClinic"),
    path("findDoctor/", views.findDoctor, name="findDoctor"),
    path("doctorDetail/", views.detailDoctor, name="doctorDetail"),
]
