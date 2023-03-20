from django.shortcuts import render
from django.http import HttpResponse
from appjulia.models import Usuario


# Create your views here.

def ingresa_usuario(request):
    nuevo_usuario = Usuario(nombre = "Fatima", apellido = "Flores", DNI = "35701813")
    nuevo_usuario.save()
    texto = f"Hola {nuevo_usuario.nombre} {nuevo_usuario.apellido}"
    return HttpResponse(texto)

def index(request):
    return render(request, 'appjulia/index.html')

def reserva(request):
    return render(request, 'appjulia/reserva.html')

def usuario(request):
    return render(request, 'appjulia/usuario.html')