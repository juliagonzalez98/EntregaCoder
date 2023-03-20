from django import forms 

class BuscarActividad(forms.Form):
    actividad = forms.CharField(max_length=35)
