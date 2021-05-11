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

class PesoCorregidoForm(forms.ModelForm):

    client = forms.ModelChoiceField(queryset=Profile.objects.filter(user__groups__name='cliente'), label='Cliente', widget=forms.Select(attrs={
        'class': 'form-control select2'
    }))
    height = forms.FloatField(label = "Estatura (m)", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control'}))
    gender = forms.CharField(label = "Genero", required=True,widget=forms.Select(attrs={
        'class': 'custom-select mr-sm-2'
    }))

    class Meta:
        model = PesoCorregido
        fields = ["client"]

    def save(self, commit=True):
        pesocorregido = super(PesoCorregidoForm, self).save(commit=False)

        if self.cleaned_data.get('gender') == "1":
            pesocorregido.corrected_weight = 23 * (self.cleaned_data.get('height') * self.cleaned_data.get('height'))
        elif self.cleaned_data.get('gender') == "2":
            pesocorregido.corrected_weight = 21.5 * (self.cleaned_data.get('height') * self.cleaned_data.get('height'))

        if commit:
            pesocorregido.save()

        return pesocorregido

    
class GERForm(forms.ModelForm):

    client = forms.ModelChoiceField(queryset=Profile.objects.filter(user__groups__name='cliente'), label='Cliente', widget=forms.Select(attrs={
        'class': 'form-control select2'
    }))
    weight = forms.FloatField(label = "Peso (kg)", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control'}))
    size = forms.FloatField(label = "Talla (cm)", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control'}))
    age = forms.FloatField(label = "Edad (años)", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control'}))
    gender = forms.CharField(label = "Genero", required=True,widget=forms.Select(attrs={
        'class': 'custom-select mr-sm-2'
    }))
    lifestyle = forms.CharField(label = "Estilo de Vida", required=True,widget=forms.Select(attrs={
        'class': 'custom-select mr-sm-2'
    }))

    class Meta:
        model = GER
        fields = ["client"]

    def save(self, commit=True):
        ger = super(GERForm, self).save(commit=False)

        if self.cleaned_data.get('gender') == "1":
            ger.ger = (9.99 * self.cleaned_data.get('weight')) + (6.25 * self.cleaned_data.get('size')) - (4.92 * self.cleaned_data.get('age')) + 5
        elif self.cleaned_data.get('gender') == "2":
            ger.ger = (9.99 * self.cleaned_data.get('weight')) + (6.25 * self.cleaned_data.get('size')) - (4.92 * self.cleaned_data.get('age')) - 161

        if self.cleaned_data.get('lifestyle') == "1":
            ger.get = ger.ger * 1.545
        elif self.cleaned_data.get('lifestyle') == "2":
            ger.get = ger.ger * 1.845
        elif self.cleaned_data.get('lifestyle') == "3":
            ger.get = ger.ger * 2.2

        if commit:
            ger.save()

        return ger



