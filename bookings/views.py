from django.shortcuts import render, redirect
from .models import Booking, Payment
from doctors.models import DetailsDoctor, Schedule
from accounts.models import AllCode
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from icecream import ic

CustomUser = get_user_model()


def BookingPageView(request, doctor, schedule):
    doctor = DetailsDoctor.objects.get(id=doctor)
    schedule = Schedule.objects.get(id=schedule)
    return render(
        request,
        "bookings/BookingPage.html",
        {"doctor": doctor, "schedule": schedule},
    )


def SaveBooking(request):
    if request.method == "POST":
        doctor = CustomUser.objects.get(id=request.POST.get("doctor_id"))
        patient = CustomUser.objects.get(id=request.POST.get("patient_id"))
        schedule = Schedule.objects.get(id=request.POST.get("schedule_id"))
        status = AllCode.objects.get(value="Chờ tiếp nhận")
        booking = Booking(
            patient=patient,
            doctor=doctor,
            schedule=schedule,
            status=status,
            examination_reason=request.POST.get("examination_reason"),
        )
        booking.save()
        request.session["booking_id"] = booking.id
    return JsonResponse({})


def PaymentView(request):

    book = Booking.objects.get(id=request.session["booking_id"])
    methods = AllCode.objects.filter(type="Method")
    return render(
        request, "bookings/paymentForm.html", {"booking": book, "methods": methods}
    )


def SavePayment(request):
    if request.method == "POST":
        booking = Booking.objects.get(id=request.POST.get("booking_id"))
        method = AllCode.objects.get(value=request.POST.get("method"))
        total = request.POST.get("total")
        status = AllCode.objects.get(value="Chưa thanh toán")
        payment = Payment(booking=booking, method=method, total=total, status=status)
        payment.save()
    return JsonResponse({})
