from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime

# Create your models here.

class Appointment(models.Model):
    client = models.ForeignKey(User, on_delete = models.CASCADE, related_name='cita')
    date = models.DateField(null=True, blank=True, verbose_name="Fecha de cita")
    hour = models.TimeField(null=True, blank=True, verbose_name="Hora de la cita")
    commentary = models.TextField(max_length=150, null = True, blank= True, verbose_name="Comentario de Cita")

    def endhour(self):
        return datetime.combine(self.date, self.hour) + timedelta(hours=1)


    class Meta:
        ordering = ['commentary']
