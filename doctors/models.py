from django.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField
from martor.models import MartorField


class Schedule(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="schedules"
    )
    time_slot = models.ForeignKey("accounts.AllCode", on_delete=models.CASCADE)
    max_number = models.SmallIntegerField()
    date = models.DateField()
    current_number = models.SmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "schedules"

    def __str__(self):
        return self.doctor.username


class DetailsDoctor(models.Model):
    doctor = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="details"
    )
    clinic = models.ForeignKey(
        "clinics.Clinic", on_delete=models.PROTECT, related_name="clinic_doctors"
    )
    specialists = models.ManyToManyField(
        "specialists.Specialist", related_name="specialist_doctors"
    )
    degree = models.ForeignKey(
        "accounts.AllCode",
        on_delete=models.PROTECT,
        related_name="degree_doctors",
        blank=True,
    )
    descriptions = MartorField(blank=True)
    background = MartorField(blank=True)
    examination_price = MoneyField(
        max_digits=19, decimal_places=4, default_currency="VND", null=True, blank=True
    )
    examination_price_note = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "details_doctors"

    def __str__(self):
        return self.doctor.username
