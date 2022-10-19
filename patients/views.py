from django.shortcuts import render

# Create your views here.
def indexPatient(request):
    return render(request,'patients/base.html')

def schedule(request):
    return render(request,'patients/schedule.html')

def historyPatient(request):
    return render(request,'patients/historyPatient.html')

def findDoctor(request):
    return render(request,'patients/FindDoctor.html')