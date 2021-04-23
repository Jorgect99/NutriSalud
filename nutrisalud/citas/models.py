from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Appointment(models.Model):
    client = models.ForeignKey(User, on_delete = models.CASCADE, related_name='cita')
    date = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de cita")
    commentary = models.TextField(max_length=150, null = True, blank= True, verbose_name="Comentario de Cita")

    class Meta:
        ordering = ['commentary']
