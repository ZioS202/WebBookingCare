from django.contrib import admin
from .models import Schedule, DetailsDoctor


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["doctor", "time_slot", "date"]


class DetailsDoctorAdmin(admin.ModelAdmin):
    list_display = ["doctor", "clinic"]


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(DetailsDoctor, DetailsDoctorAdmin)
