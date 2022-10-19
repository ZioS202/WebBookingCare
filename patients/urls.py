from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexPatient,name='index'),
    path('schedule/',views.schedule,name='schedule'),
    path('historyPatient/',views.historyPatient,name='historyPatient'),
    path('findDoctor/',views.findDoctor,name='findDoctor'),
    
]