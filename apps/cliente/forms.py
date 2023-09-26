from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut' , 'nombres' , 'apellido_paterno' , 'apellido_materno' , 'email' , 'telefono' , 'direccion']
        labels = {
            'rut' : 'Rut',
            'nombres' : 'Nombres',
            'apellido_paterno' : 'Apellido Paterno',
            'apellido_materno' : 'Apellido Materno',
            'email' : 'Correo Electronico',
            'telefono' : 'Numero de telefono',
            'direccion' : 'Direccion de vivienda'
        }
        widgets = {
            'rut' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el RUT del cliente',
                    'id' : 'rut',
                } 
            ),
            'nombres' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese nombres del cliente',
                    'id' : 'nombres',
                } 
            ),
            'apellido_paterno' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese apellido paterno del cliente',
                    'id' : 'apellido_paterno',
                } 
            ),
            'apellido_materno' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese apellido materno del cliente',
                    'id' : 'apellido_materno',
                } 
            ),
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el correo electronico del cliente',
                    'id' : 'email',
                } 
            ),
            'telefono' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el telefono del cliente',
                    'id' : 'telefono',
                } 
            ),
            'direccion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese la direccion del cliente',
                    'id' : 'direccion',
                } 
            ),
        }