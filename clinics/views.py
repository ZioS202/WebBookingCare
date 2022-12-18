from django.views.generic import DetailView
from django.shortcuts import render
from .models import Clinic
from doctors.models import DetailsDoctor
from clinics.models import Clinic
from homepage.views import SearchForm


# Create your views here.


def list_clinics(request):
    clinic_list = Clinic.objects.all()
    form = SearchForm()
    return render(
        request, "clinics/find_clinic.html", {"clinic_list": clinic_list, "form": form}
    )

class ClinicDetail(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["doctors"] = DetailsDoctor.objects.all()
        context["clinic"] = Clinic.objects.all()
        return context

    template_name = "clinics/clinic_detail.html"
    model = Clinic
    context_object_name = "clinics"
