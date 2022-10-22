from django.urls import path

import doctors
from . import views
urlpatterns = [
    path('',views.historyPatient,name='historyPatient'),

]