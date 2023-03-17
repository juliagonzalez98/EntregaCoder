from django.urls import path
from appjulia.views import saludo, ingresa_usuario, index

urlpatterns = [
    path('inicio', saludo),
    path ('ingresa_usuario/', ingresa_usuario),
    path('index/', index),
]
