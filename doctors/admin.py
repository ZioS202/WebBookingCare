from django.db import models
from django.contrib import admin
from martor.widgets import AdminMartorWidget
from martor.models import MartorField
from .models import Schedule, DetailsDoctor


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["doctor", "time_slot", "date"]


class DetailsDoctorAdmin(admin.ModelAdmin):
    list_display = ["doctor", "clinic"]
    formfield_overrides = {
        MartorField: {"widget": AdminMartorWidget},
        models.TextField: {"widget": AdminMartorWidget},
    }


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(DetailsDoctor, DetailsDoctorAdmin)
