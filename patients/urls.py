from django.urls import path

import doctors
from . import views

urlpatterns = [
    path("history/", views.historyPatient, name="historyPatient"),
]
