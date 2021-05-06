from django import forms
from .models import *
from django.contrib.auth.models import User

class IMCForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Profile.objects.filter(user__groups__name='cliente'), label='Cliente', widget=forms.Select(attrs={
        'class': 'form-control select2'
    }))
    weight = forms.FloatField(label = "Peso (kg)", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control'}))
    height = forms.FloatField(label = "Estatura (m)", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control'}))

    class Meta:
        model = IMC
        fields = ["client"]

    def save(self, commit=True):
        imc = super(IMCForm, self).save(commit=False)

        imc.imc = self.cleaned_data.get('weight') / (self.cleaned_data.get('height') * self.cleaned_data.get('height'))

        if imc.imc < 18.5:
            imc.weight_level = "Bajo Peso"
        elif imc.imc < 25:
            imc.weight_level = "Normal"
        elif imc.imc < 29.9:
            imc.weight_level = "Sobrepeso"
        else:
            imc.weight_level = "Obeso"
        if commit:
            imc.save()

        return imc



    
    



