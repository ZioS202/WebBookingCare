from http.client import ImproperConnectionState
from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexDoctor(request):
    return render(request,'doctors/base.html')
def findDoctor(request):
    return render(request,'doctors/FindDoctor.html')

def detailDoctor(request):
    return render(request,'doctors/DetailDoctor.html')

def historyDoctor(request):
    return render(request, 'doctors/HistoryDoctor.html')

def manageClinic(request):
    return render(request, 'doctors/manageClinic.html')