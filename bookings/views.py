from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User
from .models import Booking, Payment
from doctors.models import DetailsDoctor, Schedule

# Create your views here.

class BookingPageView(TemplateView):
    template_name = "bookings/BookingPage.html"