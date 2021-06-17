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

class Dieta(models.Model):

    client = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='dieta')
    vegetables = models.PositiveSmallIntegerField(verbose_name = "Verduras")
    fruits = models.PositiveSmallIntegerField(verbose_name = "Frutas")
    skim_milk = models.PositiveSmallIntegerField(verbose_name = "Leche descremada")
    low_fat_milk = models.PositiveSmallIntegerField(verbose_name = "Leche semidescremada")
    cereals_and_tubers_s = models.PositiveSmallIntegerField(verbose_name = "Cereales y Tuberculos (s/g)")
    cereals_and_tubers_c = models.PositiveSmallIntegerField(verbose_name = "Cereales y Tuberculos (c/g)")
    legumes = models.PositiveSmallIntegerField(verbose_name = "Leguminosas")
    whole_milk = models.PositiveSmallIntegerField(verbose_name = "Leche entera")
    sugars_s = models.PositiveSmallIntegerField(verbose_name = "Azucares s/g")
    sugars_c = models.PositiveSmallIntegerField(verbose_name = "Azucares c/g")
    protein_mbg = models.PositiveSmallIntegerField(verbose_name = "Proteinas AOA mbg")
    protein_bg = models.PositiveSmallIntegerField(verbose_name = "Proteinas AOA bg")
    oils_and_fats_s = models.PositiveSmallIntegerField(verbose_name = "Aceites y grasas s/p")
    oils_and_fats_c = models.PositiveSmallIntegerField(verbose_name = "Aceites y grasas c/p")
    protein_mg = models.PositiveSmallIntegerField(verbose_name = "Proteinas AOA mg")
    protein_ag = models.PositiveSmallIntegerField(verbose_name = "Proteinas AOA ag")

    kcal_carbohidratos = models.FloatField(default=0 , verbose_name = "Kcal Carbohidratos")
    kcal_proteinas = models.FloatField(default=0 , verbose_name = "Kcal Proteinas")
    kcal_lipidos = models.FloatField(default=0 , verbose_name = "Kcal Lipidos")
    distribucion_carbohidratos = models.FloatField(default=0 , verbose_name = "Distribucion Carbohidratos")
    distribucion_proteinas = models.FloatField(default=0 , verbose_name = "Distribucion Proteinas")
    distribucion_lipidos = models.FloatField(default=0 , verbose_name = "Distribucion Lipidos")
    kcal_total = models.FloatField(default=0 , verbose_name = "Kcal TOTAL")

    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Agregado")

    class Meta:
        ordering = ['-created']