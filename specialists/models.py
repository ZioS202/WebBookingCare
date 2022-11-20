from django.db import models
from django.conf import settings
from martor.models import MartorField


class Specialist(models.Model):
    name = models.CharField(max_length=50)
    description = MartorField(blank=True)
    avatar = models.ImageField(upload_to="avatars_specialist/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "specialists"

    def __str__(self):
        return self.name
