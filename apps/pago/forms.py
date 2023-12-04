from django import forms
from .utils import formatear_monto
from .models import Pago

class PagoForm(forms.ModelForm):
    
    class Meta:
        model = Pago
        fields = ['credito', 'monto_pagado', 'fecha_pago', 'estado_pago', 'tipo_pago']
        labels = {
            'credito' : 'Credito',
            'monto_pagado' : 'Monto pagado',
            'fecha_pago' : 'Fecha de pago',
            'estado_pago' : 'Estado pago',
            'tipo_pago' : 'Tipo pago',
        }
        widgets = {
            'credito' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Seleccione el credito del pago',
                    'id' : 'credito-pago',
                } 
            ),
            'monto_pagado' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el monto del pago',
                    'id' : 'monto_pagado',
                } 
            ),
            'fecha_pago' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date',
                    'placeholder' : 'Seleccione la fecha del pago',
                    'id' : 'fecha_pago',
                } 
            ),
            'estado_pago' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Seleccione el estado del pago',
                    'id' : 'estado_pago',
                } 
            ),
            'tipo_pago' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Seleccione el tipo de pago',
                    'id' : 'tipo_pago',
                } 
            ),
        }

    def clean_monto_pagado(self):
        monto_pagado = self.cleaned_data.get('monto_pagado')

        monto_pagado_formateado = formatear_monto(monto_pagado)

        self.cleaned_data['monto_pagado'] = monto_pagado_formateado

        return monto_pagado_formateado