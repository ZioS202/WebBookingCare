from django import template
from homepage.forms import SearchForm
from django.http import JsonResponse
from specialists.models import Specialist
from icecream import ic

register = template.Library()


@register.inclusion_tag("homepage/search.html", takes_context=True)
def specialist_search(context):
    query = None
    data = {}
    results = []
    request = context["request"]
    if "query" in request.GET:
        query = request.GET.get("query")
        results = Specialist.objects.filter(name__icontains=query)
        ic(results)
    for result in results:
        data.update({result.id: {"name": result.name, "avatar": ""}})
    ic(data)
    return JsonResponse(data)


@register.simple_tag
def homepage_search(context):
    request = context["request"]
    ic(request.GET.get("query"))
    query = request.GET.get("query")
    data = {
        "results": Specialist.objects.filter(
            name__icontains=query, description__icontains=query
        )
    }
    return JsonResponse(data)
