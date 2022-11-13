from django.contrib import admin
from .models import Booking, Payment


class BookingAdmin(admin.ModelAdmin):
    list_display = ["patient", "doctor", "schedule", "status"]


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["booking", "status"]


admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PaymentAdmin)
