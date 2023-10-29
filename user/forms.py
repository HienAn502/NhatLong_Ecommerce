from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms, EmailField


class CustomUserCreationForm(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields
