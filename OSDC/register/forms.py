from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    DOCTOR = 'D'
    PATIENT = 'P'
    TYPE_CHOICES = (
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
    )
    group = forms.ChoiceField(label="Doctor or patient", choices = TYPE_CHOICES)
    email = forms.EmailField()
    first_name = forms.CharField(label="first name")
    last_name = forms.CharField(label="last name")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name", "group"]