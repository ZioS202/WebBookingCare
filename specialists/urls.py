from django.urls import path
from . import views

urlpatterns = [
    path("findSpecialist/", views.find_specialist, name="findSpecialist"),
    path("specialistDetail/", views.specialist_detail, name="specialistDetail"),
]
