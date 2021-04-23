from django import forms
from .models import Appointment
from registration.models import Profile
from django.contrib.auth.models import User


class AppointmentForm(forms.ModelForm):
    phone = forms.CharField(label='Telefono:', max_length=10)

    class Meta:
        model = Appointment
        fields = ["date", "commentary"]

    def save(self, commit=True, request = None):
        appointment = super(AppointmentForm, self).save(commit=False)

        appointment.client = request.user
        
        if commit:
            request.user.profile.phone = self.cleaned_data['phone']
            request.user.profile.save()
            appointment.save()

        return appointment

    
