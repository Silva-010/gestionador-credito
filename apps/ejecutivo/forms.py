from django import forms
from .models import Ejecutivo

class EjecutivoForm(forms.ModelForm):
    class Meta:
        model = Ejecutivo
        fields = ['id_banco' , 'nombre' , 'apellido_paterno' , 'apellido_materno' , 'email' , 'telefono']
        labels = {
            'id_banco' : 'Banco',
            'nombre' : 'Nombres',
            'apellido_paterno' : 'Apellido Paterno',
            'apellido_materno' : 'Apellido Materno',
            'email' : 'Correo Electronico',
            'telefono' : 'Numero de telefono',
        }
        widgets = {
            'id_banco' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Seleccione el banco al que pertenece el ejecutivo',
                    'id' : 'id_banco',
                } 
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese nombres del ejecutivo',
                    'id' : 'nombres',
                } 
            ),
            'apellido_paterno' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese apellido paterno del ejecutivo',
                    'id' : 'apellido_paterno',
                } 
            ),
            'apellido_materno' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese apellido materno del ejecutivo',
                    'id' : 'apellido_materno',
                } 
            ),
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el correo electronico del ejecutivo',
                    'id' : 'email',
                } 
            ),
            'telefono' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el telefono del ejecutivo',
                    'id' : 'telefono',
                } 
            ),
        }