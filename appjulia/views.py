from django.shortcuts import render
from django.http import HttpResponse
from appjulia.models import *
from appjulia.forms import *


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

def guardar_usuario(request):
         if request.method == "POST":
 
            usuario = GuardaUsuarioForm(request.POST) 
            print(usuario)
 
            if usuario.is_valid:
                  informacion = usuario.cleaned_data
                  usuario = Usuario(nombre=informacion["nombre"], camada=informacion["apellido"])
                  usuario.save()
                  return render(request, "AppCoder/inicio.html")
         else:
            usuario = GuardaUsuarioForm()
 
         return render(request, "appjulia/FormUsuariohtml", {"usuario": usuario})


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

def BuscaUsuario(request):
        if request.method == "POST":
            usuario = BuscarUsuarioForm(request.POST) 
            print(usuario)

            if usuario.is_valid:
                  informacion = usuario.cleaned_data
                  usuarios = Usuario.objects.filter(nombre = informacion["nombre"])
                  return render(request, "appjuliaj/BuscaUsuario.html", {"data":[usuarios]})
             
        else:
              usuario = GuardaUsuarioForm()

        return render(request, 'appjulia/BuscaUsuario.html', {"usuario": usuario})

