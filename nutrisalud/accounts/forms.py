from django.contrib.auth.hashers import make_password

from django import forms
from .models import Profile
from django.contrib.auth.models import User


# Create your forms here.

class LoginForm(forms.Form):
    email = forms.CharField(label='Correo electrónico:', max_length=100)
    password = forms.CharField(label='Contraseña:', max_length=100)

class SignupForm(forms.ModelForm):
    last_name_m = forms.CharField(label='Apellido Materno:', max_length=100)
    password = forms.CharField(label='Contraseña:', max_length=100)
    password2 = forms.CharField(label='Repetir Contraseña:', max_length=100)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

        labels = {
            'first_name': 'Nombre(s):',
            'last_name': 'Apellido Paterno:',
            'email': 'Correo electrónico:',
        }

    def clean(self):
        data = super(SignupForm, self).clean()
        if 'password' in data and data['password'] != data['password2']:
            raise ValidationError("Contraseñas no coinciden")

    def save(self, commit=True):
        u = super(SignupForm, self).save(commit=False)

        if not u.id:
            u.password = make_password(self.cleaned_data['password'])
            u.username = u.email
        if commit:
            u.save()

        self.instance.profile = Profile()
        self.instance.profile.last_name_m = self.cleaned_data.get('last_name_m')
        self.instance.profile.save()

        return u

    

    