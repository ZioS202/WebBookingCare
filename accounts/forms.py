from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    # phone_number = PhoneNumberField(region="VN")

    class Meta:
        model = get_user_model()
        fields = UserChangeForm.Meta.fields
