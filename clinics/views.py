from django.views.generic import TemplateView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Clinic
from doctors.models import DetailsDoctor
from clinics.models import Clinic


# Create your views here.

def list_clinics(request):
    clinic_list = Clinic.objects.all()
    return render(request, "clinics/find_clinic.html", {"clinic_list": clinic_list} )

# class FindClinic(TemplateView):
#     template_name = "clinics/find_clinic.html"

class ClinicDetail(DetailView):
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['doctors'] = DetailsDoctor.objects.all()
        context['clinic'] = Clinic.objects.all()
        return context
    template_name = "clinics/clinic_detail.html"
    model = Clinic
    context_object_name = "clinics"
