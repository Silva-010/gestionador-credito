from django import forms
from .utils import formatear_monto
from .models import SolicitudCredito

class SolicitudForm(forms.ModelForm):
    
    class Meta:
        model = SolicitudCredito
        fields = ['cliente', 'banco', 'monto_solicitado','fecha_solicitud','estado_solicitud','fecha_aprobacion','tipo_credito']
        labels = {
            'cliente' : 'Cliente',
            'banco' : 'Banco',
            'monto_solicitado' : 'Monto Solicitado',
            'fecha_solicitud' : 'Fecha Solicitud',
            'estado_solicitud' : 'Estado Solicitud',
            'fecha_aprobacion' : 'Fecha Aprovación',
            'tipo_credito' : 'Tipo Credito',
        }
        input_formats=['%d-%m-%Y']
        widgets = {
            'cliente' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Seleccione al cliente de la solicitud',
                    'id' : 'cliente-solicitud',
                } 
            ),
            'banco' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Seleccione el banco donde se realizo la solicitud',
                    'id' : 'banco-solicitud',
                } 
            ),
            'monto_solicitado' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el monto solicitado',
                    'id' : 'monto_solicitado',
                } 
            ),
            'fecha_solicitud' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date',
                    'placeholder' : 'Seleccione fecha de la solicitud',
                    'id' : 'fecha_solicitud',
                },
                format='%d-%m-%Y',
            ),
            'estado_solicitud' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Seleccione el estado de la solicitud',
                    'id' : 'estado_solicitud',
                } 
            ),
            'fecha_aprobacion' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date',
                    'placeholder' : 'Seleccione la fecha de aprobación',
                    'id' : 'fecha_aprobacion',
                } 
            ),
            'tipo_credito' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Seleccione el tipo de credito',
                    'id' : 'tipo_credito',
                } 
            ),
        }

    def clean_monto_solicitado(self):
        monto_solicitado = self.cleaned_data.get('monto_solicitado')

        monto_solicitado_formateado = formatear_monto(monto_solicitado)

        self.cleaned_data['monto_solicitado'] = monto_solicitado_formateado

        return monto_solicitado_formateado