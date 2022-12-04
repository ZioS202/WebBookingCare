from django.shortcuts import render
from django.views.generic import TemplateView
from specialists.models import Specialist
from clinics.models import Clinic
from doctors.models import DetailsDoctor
from homepage.forms import SearchForm
from django.http import JsonResponse
from icecream import ic


# from icecream import ic

# Create your views here.


class HomePageView(TemplateView):
    template_name = "homepage/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["specialists"] = Specialist.objects.all()
        context["clinics"] = Clinic.objects.all()
        context["doctors"] = DetailsDoctor.objects.all()
        context["form"] = SearchForm()
        return context


def search_specialist(request):
    query = None
    data = {}
    results = []
    if "query" in request.GET:
        query = request.GET.get("query")
        results = Specialist.objects.filter(name__icontains=query)
    for result in results:
        data.update({result.id: {"name": result.name, "avatar": result.avatar.url}})
    return JsonResponse(data)


def search_clinic(request):
    query = None
    data = {}
    results = []
    if "query" in request.GET:
        query = request.GET.get("query")
        results = Clinic.objects.filter(name__icontains=query)
    for result in results:
        data.update(
            {result.id: {"name": result.name, "avatar": result.Cover_photo.url}}
        )
    return JsonResponse(data)


def search_doctor(request):
    query = None
    data = {}
    results = []
    if "query" in request.GET:
        query = request.GET.get("query")
        results1 = DetailsDoctor.objects.filter(doctor__first_name__icontains=query)
        results2 = DetailsDoctor.objects.filter(doctor__last_name__icontains=query)
    if results1:
        for result in results1:
            data.update(
                {
                    result.id: {
                        "name": result.degree.value
                        + " "
                        + result.doctor.last_name
                        + " "
                        + result.doctor.first_name,
                        "avatar": result.doctor.avatar.url,
                    }
                }
            )
    elif results2:
        for result in results2:
            data.update(
                {
                    result.id: {
                        "name": result.degree.value
                        + " "
                        + result.doctor.last_name
                        + " "
                        + result.doctor.first_name,
                        "avatar": result.doctor.avatar.url,
                    }
                }
            )
    return JsonResponse(data)
