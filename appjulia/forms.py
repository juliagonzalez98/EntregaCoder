from django import forms 

class BuscarTurnoActividadForm (forms.Form):
    turno = forms.CharField(max_length=10)

