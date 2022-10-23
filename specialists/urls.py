from django.urls import path
from . import views
urlpatterns = [
    path('find_specialist/',views.find_specialist, name='find_specialist'),
    path('specialist_detail/',views.specialist_detail, name='specialist_detail'),
]