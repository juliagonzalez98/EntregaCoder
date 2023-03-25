from django import forms 

class GuardaUsuarioForm (forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)

class BuscarUsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)   
     
