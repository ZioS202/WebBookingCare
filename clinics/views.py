from django.views.generic import TemplateView

# Create your views here.


class ClinicDetail(TemplateView):
    template_name = "clinics/clinic_detail.html"

class FindClinic(TemplateView):
    template_name = "clinics/find_clinic.html"
