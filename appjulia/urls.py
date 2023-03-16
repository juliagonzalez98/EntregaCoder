from django.urls import path
from appjulia.views import saludo, ingresa_usuario

urlpatterns = [
    path('inicio', saludo),
    path ('ingresa_usuario/', ingresa_usuario),
]
