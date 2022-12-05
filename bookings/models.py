from django.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField


class Booking(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_bookings",
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_bookings",
    )
    status = models.ForeignKey(
        "accounts.AllCode", on_delete=models.PROTECT, related_name="status_bookings"
    )
    schedule = models.ForeignKey(
        "doctors.Schedule", on_delete=models.CASCADE, related_name="schedule_bookings"
    )
    examination_reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "bookings"

    def __str__(self):
        return self.patient.username + " - " + self.doctor.username


class Payment(models.Model):
    booking = models.OneToOneField(
        Booking, on_delete=models.CASCADE, related_name="payment"
    )
    method = models.ForeignKey(
        "accounts.AllCode", on_delete=models.PROTECT, related_name="method_payments"
    )
    status = models.ForeignKey(
        "accounts.AllCode", on_delete=models.PROTECT, related_name="status_payments"
    )
    total = MoneyField(max_digits=19, decimal_places=4, default_currency="VND")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "payments"

    def __str__(self):
        return self.booking.patient.username + " - " + self.booking.doctor.username
