from django import forms
from .models import Cliente
from .validations import validar_rut_chileno, formatear_rut, validar_telefono_chileno, formatear_telefono_chileno

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['rut' , 'nombres' , 'apellido_paterno' , 'apellido_materno' , 'email' , 'telefono' , 'direccion']
        labels = {
            'rut' : 'Rut',
            'nombres' : 'Nombres',
            'apellido_paterno' : 'Apellido Paterno',
            'apellido_materno' : 'Apellido Materno',
            'email' : 'Correo Electrónico',
            'telefono' : 'Número de teléfono',
            'direccion' : 'Dirección de vivienda'
        }
        widgets = {
            'rut' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : '11.111.111-1',
                    'id' : 'rut',
                } 
            ),
            'nombres' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Juan',
                    'id' : 'nombres',
                } 
            ),
            'apellido_paterno' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Perez',
                    'id' : 'apellido_paterno',
                } 
            ),
            'apellido_materno' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Perez',
                    'id' : 'apellido_materno',
                } 
            ),
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'correo@tudominio.cl',
                    'id' : 'email',
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
            'direccion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Calle La Moneda 123',
                    'id' : 'direccion',
                } 
            ),
        }

    error_messages = {
        'nombres': {
            'required': 'El nombre es obligatorio.',
        },
    }
        
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')

        # Utiliza la función validar_rut_chileno para validar el campo "rut"
        if not validar_rut_chileno(rut):
            raise forms.ValidationError("El RUT no es válido. Por favor, ingrese un RUT chileno válido.")

        # Formatea el RUT utilizando la función formatear_rut
        rut_formateado = formatear_rut(rut)

        # Actualiza el valor del campo "rut" en los datos limpios (cleaned_data)
        self.cleaned_data['rut'] = rut_formateado

        return rut_formateado
    
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