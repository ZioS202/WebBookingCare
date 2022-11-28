from django.urls import path
from .views import BookingPageView

urlpatterns = [
    path("", BookingPageView.as_view(), name="bookings"),
]
