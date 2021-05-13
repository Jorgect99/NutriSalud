from django.db import models
from django.contrib.auth.models import User
from registration.models import Profile

# Create your models here.

class IMC(models.Model):

    client = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='imc')
    imc = models.FloatField(verbose_name = "IMC", default=0)
    weight_level = models.CharField(max_length=30, verbose_name = "Nivel de Peso")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Calculo")

    class Meta:
        ordering = ['-created']

class PesoCorregido(models.Model):

    client = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='pesocorregido')
    corrected_weight = models.FloatField(verbose_name = "Peso Corregido", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Calculo")

    class Meta:
        ordering = ['-created']


class GER(models.Model):

    client = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='ger')
    ger = models.FloatField(verbose_name = "Requerimiento Energético en Reposo", default=0)
    get = models.FloatField(verbose_name = "Requerimiento Energético Total", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Calculo")

    class Meta:
        ordering = ['-created']

class Food_Group(models.Model):

    food_group = models.CharField(max_length=255, verbose_name = "Grupo de Alimentos")
    food = models.CharField(max_length=255, verbose_name = "Alimento")
    amount = models.FloatField(default=0 , verbose_name = "Cantidad")
    unit = models.CharField(max_length=255, verbose_name = "Unidad")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Agregado")
    
    def get_amount(self):
        return "{:.3g} {}".format(self.amount, self.unit) 

    class Meta:
        ordering = ['-created']