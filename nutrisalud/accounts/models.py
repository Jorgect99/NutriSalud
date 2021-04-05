from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/'+filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    last_name_m = models.CharField(max_length=150, blank=True, verbose_name="Segundo Apellido")
    phone = models.CharField(max_length=10, blank=True, verbose_name="Teléfono")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento")
    avatar = models.ImageField(upload_to = custom_upload_to, null = True, blank = True, verbose_name="Avatar")
    bio = models.TextField(null = True, blank= True, verbose_name="Biografia")

    class Meta:
        ordering = ['user__username']
