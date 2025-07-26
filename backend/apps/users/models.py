from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.ubication.models import Ubication
# Create your models here.

# Extendemos mediante AbstracBaseUser los metodos y atribudos del modelo User por defecto
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, verbose_name="Email", unique=True)
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=50, unique=True, blank=True)
    bank_count = models.CharField(max_length=12, blank=True)
    ubication = models.OneToOneField(Ubication, related_name="user", on_delete=models.PROTECT, null=True)

    #Especificamos caul va a ser el reemplazo de username y cuales son los requeridos
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "username"]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"