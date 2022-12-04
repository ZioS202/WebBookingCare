from django.views.generic import TemplateView, DetailView
from http.client import ImproperConnectionState
from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from .models import DetailsDoctor, Schedule
from clinics.models import Clinic
from specialists.models import Specialist


# Create your views here.

def indexDoctor(request):
    return render(request,'doctors/base.html')

def findDoctor(request):
    doctor_list = DetailsDoctor.objects.all()
    return render(request,'doctors/FindDoctor.html', {'doctor_list': doctor_list})

# def detailDoctor(request):
#     return render(request,'doctors/DetailDoctor.html')

class DoctorDetail(DetailView):
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['specialists'] = Specialist.objects.all()
        context['clinic'] = Clinic.objects.all()
        context['schedule'] = Schedule.objects.all()
        return context
    template_name = "doctors/DetailDoctor.html"
    model = DetailsDoctor
    context_object_name = "doctor"

# def manageClinic(request):
#     return render(request, 'doctors/manageClinic.html')