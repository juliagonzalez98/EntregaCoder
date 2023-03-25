from django.shortcuts import render
from django.http import HttpResponse
from appjulia.models import *


# Create your views here.

def index(request):
    return render(request, 'appjulia/index.html')

def reserva(request):
    return render(request, 'appjulia/reserva.html')

def usuario(request):
    return render(request, 'appjulia/usuario.html')

def actividad(request):
    return render(request, 'appjulia/actividad.html')

def FormularioUsuario(request):

    if request.method == "POST":
        print ("\n\n{request.POST}\n\n")
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        usuario = Usuario(nombre = nombre, apellido = apellido)
        usuario.save()

    return render(request, "appjulia/FormularioUsuario.html")

def EligeActividad (request):
    if request.method == "POST":
        print("\n\n {request.POST} \n\n")
        actividad= request.POST["actividad"]
        actividad = Actividad(actividad = actividad) 
        actividad.save()

    return render(request, 'appjulia/EligeActividad.html')

def BuscaTurno (request):
    if request.method == "POST":
        print("\n\n {request.POST} \n\n")
        turno = request.POST["turno"]
        turno = Reserva(turno = turno) 
        turno.save()
    return render (request, 'appjulia/BuscaTurno.html') 

