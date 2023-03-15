from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    DNI = models.CharField(max_length=15)
    
class Actividad(models.Model):
    actividad_elegida = models.CharField(max_length=35)
    clase = models.CharField(max_length=1)

class Reserva(models.Model):
     turno = models.CharField(max_length=5)


    