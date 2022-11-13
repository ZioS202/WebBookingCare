from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class AllCode(models.Model):
    type = models.CharField(max_length=20)
    value = models.CharField(max_length=50)

    class Meta:
        db_table = "all_codes"

    def __str__(self):
        return self.value


class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    phone_number = PhoneNumberField(max_length=16, blank=True)
    gender = models.ForeignKey(
        AllCode,
        on_delete=models.PROTECT,
        related_name="users",
        blank=True,
        null=True,
    )
    birthdate = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars_user/", blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
