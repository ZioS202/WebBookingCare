from http.client import ImproperConnectionState
from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from .models import Specialist
from doctors.models import DetailsDoctor
from clinics.models import Clinic
from django.views.generic import TemplateView, DetailView
# Create your views here.

def list_specialists(request):
    specialist_list = Specialist.objects.all()
    return render(request,'specialists/find_specialist.html', {'specialist_list':specialist_list})

# def specialist_detail(request, name):
#     specialist = Specialist.objects.get(name=name)
#     return render(request,'specialists/specialist_detail.html', {'specialist': specialist})

class Specialist_Detail(DetailView):
    def get_context_data(self, **kwargs):
        # name=self.request.GET.get("name")
        context=super().get_context_data(**kwargs)
        # context['specialist'] = Specialist.objects.get(name=name)
        context['doctors'] = DetailsDoctor.objects.all()
        context['clinic'] = Clinic.objects.all()
        return context
    template_name = "specialists/specialist_detail.html"
    model = Specialist
    context_object_name = "specialist"
