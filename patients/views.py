from django.shortcuts import render

# Create your views here.
def historyPatient(request):
    return render(request, "patients/historyPatient.html")
