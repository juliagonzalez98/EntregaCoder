from django.urls import path
from appjulia.views import *

urlpatterns = [
    path('', index, name="index"),
    path('reserva/', reserva, name="reserva"),
    path('usuario/', usuario, name= "usuario"),
    path('formulariousuario', FormularioUsuario, name= "FormularioUsuario"),
    path('actividad', actividad, name= "actividad"),
    path('EligeActividad', EligeActividad, name="EligeActividad"),
    path('BuscaTurno', BuscaTurno, name="BuscaTurno"),
]
