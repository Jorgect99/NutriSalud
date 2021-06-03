from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from django import forms
from .models import Profile
from django.contrib.auth.models import User


# Create your forms here.

class LoginForm(forms.Form):
    email = forms.CharField(label='Correo electrónico:', max_length=100)
    password = forms.CharField(label='Contraseña:', max_length=100)

class SignupForm(forms.ModelForm):
    last_name_m = forms.CharField(label='Apellido Materno:', max_length=100, required=False)
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
        if not ('first_name' in data and data['first_name']):
            raise ValidationError("Se requiere Nombre")

        if 'password' in data and data['password'] != data['password2']:
            raise ValidationError("Contraseñas no coinciden, vuelve a intentar")
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email


    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        profile = {
            "last_name_m": self.cleaned_data.get('last_name_m')
        }
        user.profile = Profile(**profile)

        if not user.id:
            user.password = make_password(self.cleaned_data['password'])
            user.username = user.email
        if commit:
            user.save()
            user.profile.save()

        return user

class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(label='Nombre(s):', max_length=150)
    last_name = forms.CharField(label='Apellido Paterno:', max_length=150)
    
    class Meta:
        model = Profile
        fields = ["last_name_m", "phone", "birth_date", "avatar"]

        labels = {
            'last_name_m': 'Apellido Materno:',
            'phone': 'Teléfono:',
            'birth_date': 'Fecha de Nacimiento:',
            'avatar': 'Imagen de perfil:',
        }

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        
        profile.user.first_name = self.cleaned_data['first_name']
        profile.user.last_name = self.cleaned_data['last_name']
        
        if commit:
            profile.save()
            profile.user.save()

        return profile
