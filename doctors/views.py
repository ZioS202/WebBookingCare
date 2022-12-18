from django.views.generic import DetailView
from django.shortcuts import render
from .models import DetailsDoctor, Schedule
from django.contrib.auth import get_user_model
from homepage.views import SearchForm
from django.http import JsonResponse

CustomUser = get_user_model()

# Create your views here.


def indexDoctor(request):
    return render(request, "doctors/base.html")


def findDoctor(request):
    doctor_list = DetailsDoctor.objects.all()
    form = SearchForm()
    return render(
        request, "doctors/FindDoctor.html", {"doctor_list": doctor_list, "form": form}
    )


class DoctorDetail(DetailView):
    template_name = "doctors/DetailDoctor.html"
    model = DetailsDoctor
    context_object_name = "doctor"


def search_schedule(request):
    query = None
    doctor_id = None
    data = {}
    results = []
    if "query" in request.GET and "doctor_id" in request.GET:
        query = request.GET.get("query")
        doctor_id = request.GET.get("doctor_id")
        doctor = CustomUser.objects.get(id=doctor_id)
        results = doctor.schedules.filter(date=query)
    for result in results:
        data.update({result.id: {"time_slot": result.time_slot.value}})
    return JsonResponse(data)
