from django.shortcuts import render
from .models import Specialist
from django.views.generic import DetailView
from homepage.forms import SearchForm

# Create your views here.


def list_specialists(request):
    specialist_list = Specialist.objects.all()[:8]
    form = SearchForm()
    return render(
        request,
        "specialists/find_specialist.html",
        {
            "specialist_list": specialist_list,
            "form": form,
        },
    )

class Specialist_Detail(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    template_name = "specialists/specialist_detail.html"
    model = Specialist
    context_object_name = "specialist"
