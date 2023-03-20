from django.shortcuts import render
from django.http import HttpResponse
from appjulia.models import Usuario


# Create your views here.

def index(request):
    return render(request, 'appjulia/index.html')

def reserva(request):
    return render(request, 'appjulia/reserva.html')

def usuario(request):
    return render(request, 'appjulia/usuario.html')