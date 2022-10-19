from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexDoctor,name='index'),
    path('manageClinic/',views.manageClinic, name='manageClinic'),
    path('findDoctor/',views.findDoctor, name='findDoctor'),
    path('detailDoctor/',views.detailDoctor, name= 'detailDoctor'),
    path('historyDoctor/',views.historyDoctor, name= 'historyDoctor'),
    
]
