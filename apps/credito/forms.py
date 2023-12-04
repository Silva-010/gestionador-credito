from django import forms
from .utils import formatear_monto
from .models import Credito

class CreditoForm(forms.ModelForm):
    
    class Meta:
        model = Credito
        fields = ['solicitud_credito', 'monto', 'tasa_de_interes', 'plazo_en_meses', 'fecha_creacion', 'estado']
        labels = {
            'solicitud_credito' : 'Solicitud',
            'monto' : 'Monto',
            'tasa_de_interes' : 'Tasa de Interes',
            'plazo_en_meses' : 'Plazo (Meses)',
            'fecha_creacion' : 'Fecha creacion',
            'estado' : 'Estado',
        }
        widgets = {
            'solicitud_credito': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione la solicitud del credito',
                    'id': 'solicitud-credito',
                    'onchange': 'actualizar_monto()',
                }
            ),
            'monto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el monto del credito',
                    'id': 'monto',
                }
            ),
            'tasa_de_interes': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la tasa de interes del credito',
                    'id': 'tasa_de_interes',
                }
            ),
            'plazo_en_meses': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el plazo del credito',
                    'id': 'plazo_en_meses',
                }
            ),
            'fecha_creacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'placeholder': 'Seleccione la fecha de creacion del credito',
                    'id': 'fecha_creacion',
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione seleccione el estado del credito',
                    'id': 'estado-credito',
                }
            ),
        }

    def clean_monto(self):
        monto = self.cleaned_data.get('monto')

        monto_formateado = formatear_monto(monto)

        self.cleaned_data['monto'] = monto_formateado

        return monto_formateado