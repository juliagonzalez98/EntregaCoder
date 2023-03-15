from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    DNI = models.CharField(max_length=15)
    