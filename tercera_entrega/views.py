from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse ("Bienvenidos a FOCUS GYM. Ingrese sus datos")

def ingresa_datos(request):
    return HttpResponse("Ingrese sus datos de usuario")

def probando_template(request):
    mihtml = open("./templates/template1.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    contexto = Context()

    documento = plantilla.render(contexto)
    return HttpResponse(documento)


