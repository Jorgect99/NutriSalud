from django import forms
from .models import Appointment
from registration.models import Profile
from django.contrib.auth.models import User


class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ["date", "commentary"]

    
