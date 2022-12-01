from django.urls import path
from .views import Specialist_Detail
from . import views

urlpatterns = [
    path("findSpecialist/", views.list_specialists, name="findSpecialist"),
    # path("specialistDetail/<str:name>", views.specialist_detail, name="specialistDetail"),
    path("specialistDetail/<int:pk>", Specialist_Detail.as_view(), name="specialistDetail"),
]
