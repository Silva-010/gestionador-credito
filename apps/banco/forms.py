from django import forms
from .models import Banco

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['nombre', 'direccion', 'telefono']
        labels = {
            'nombre' : 'Nombre',
            'direccion' : 'Dirección',
            'telefono' : 'Telefono',
        }
        widgets = {
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el nombre del banco',
                    'id' : 'nombre',
                } 
            ),
            'direccion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese la dirección del banco',
                    'id' : 'direccion',
                } 
            ),
            'telefono' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el telefono del banco',
                    'id' : 'telefono',
                } 
            ),
        }