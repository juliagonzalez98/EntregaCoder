from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
   
class Actividad(models.Model):
    actividad= models.CharField(max_length=35)

    def __str__(self):
        return f"{self.actividad}"
    
class Reserva(models.Model):
     turno = models.CharField(max_length=5)

     def __str__(self):
        return f"{self.turno}"




    