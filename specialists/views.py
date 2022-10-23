from http.client import ImproperConnectionState
from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def find_specialist(request):
    return render(request,'specialists/find_specialist.html')

def specialist_detail(request):
    return render(request,'specialists/specialist_detail.html')

