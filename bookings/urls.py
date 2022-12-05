from django.urls import path
from .views import BookingPageView, SaveBooking, PaymentView, SavePayment

urlpatterns = [
    path("<int:doctor>/<int:schedule>/", BookingPageView, name="bookings"),
    path("save-booking/", SaveBooking, name="saveBooking"),
    path("payment/", PaymentView, name="paymentInfo"),
    path("save-payment/", SavePayment, name="savePayment"),
]
