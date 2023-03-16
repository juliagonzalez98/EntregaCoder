from django.shortcuts import render
from django.http import HttpResponse
from appjulia.models import Usuario


# Create your views here.

def saludo(request):
    return HttpResponse ("Bienvenidos a FOCUS GYM. Ingrese sus datos")


def ingresa_usuario(request):
    nuevo_usuario = Usuario(nombre = "Fatima", apellido = "Flores", DNI = "35701813")
    nuevo_usuario.save()
    texto = f"Hola {nuevo_usuario.nombre} {nuevo_usuario.apellido}"
    return HttpResponse(texto)