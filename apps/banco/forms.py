from django import forms
from .models import Banco
from .validations import formatear_telefono_chileno, validar_telefono_chileno

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
                    'type' : 'tel',
                    'placeholder' : '+569 9999 9999',
                    'id' : 'telefono',
                } 
            ),
        }

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        # Valida el número de teléfono
        if not validar_telefono_chileno(telefono):
            raise forms.ValidationError("El número de teléfono no es válido. Por favor, recuerde ingresar el codigo regional +569")

        # Formatea el número de teléfono
        telefono_formateado = formatear_telefono_chileno(telefono)

        # Actualiza el valor del campo "telefono" en los datos limpios (cleaned_data)
        self.cleaned_data['telefono'] = telefono_formateado

        return telefono_formateado