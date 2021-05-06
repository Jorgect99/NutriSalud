from django.db import models
from django.contrib.auth.models import User
from registration.models import Profile

# Create your models here.

class IMC(models.Model):

    client = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='imc')
    imc = models.FloatField(verbose_name = "IMC")
    weight_level = models.CharField(max_length=30, verbose_name = "Nivel de Peso")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Calculo")

    class Meta:
        ordering = ['-created']

class PesoCorregido(models.Model):

    client = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='pesocorregido')
    corrected_weight = models.FloatField(verbose_name = "Peso Corregido")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Calculo")

    class Meta:
        ordering = ['-created']


class GER(models.Model):

    client = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='ger')
    ger = models.FloatField(verbose_name = "Requerimiento Energético en Reposo")
    get = models.FloatField(verbose_name = "Requerimiento Energético Total")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Calculo")

    class Meta:
        ordering = ['-created']
