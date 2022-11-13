from django.db import models


class Clinic(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    description_html = models.TextField(blank=True)
    description_markdown = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars_clinic/", blank=True)
    Cover_photo = models.ImageField(upload_to="cover_photos_clinic/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "clinics"

    def __str__(self):
        return self.name
