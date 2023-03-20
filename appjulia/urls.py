from django.urls import path
from appjulia.views import *

urlpatterns = [
    path ('ingresa_usuario/', ingresa_usuario),
    path('', index, name="index"),
    path('reserva/', reserva, name="reserva"),
    path('usuario/', usuario, name= "usuario"),
]
