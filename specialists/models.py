from django.db import models
from django.conf import settings


class Specialist(models.Model):
    name = models.CharField(max_length=50)
    clinics = models.ManyToManyField(
        "clinics.Clinic", related_name="clinic_specialists"
    )
    doctors = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="doctor_specialists"
    )
    description_html = models.TextField(blank=True)
    description_markdown = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars_specialist/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "specialists"

    def __str__(self):
        return self.name
