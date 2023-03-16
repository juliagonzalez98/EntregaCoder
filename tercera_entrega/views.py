from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse ("Bienvenidos a FOCUS GYM. Ingrese sus datos")

def ingresa_datos(request):
    return HttpResponse("Ingrese sus datos de usuario")

def probando_template(request):
    notas = [8,6,9] #codigo que va variando
    mis_datos = {"nombre": "julia", "apellido": "gonzalez", "notas": notas} #codigo que va variando

    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(mis_datos)
    return HttpResponse(documento)


