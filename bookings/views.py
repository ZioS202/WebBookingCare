from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Create your views here.

class BookingPageView(TemplateView):
    template_name = "bookings/BookingPage.html"