from django.views.generic import TemplateView

# Create your views here.

class BookingPageView(TemplateView):
    template_name = "bookings/BookingPage.html"