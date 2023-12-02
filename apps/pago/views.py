from django.shortcuts import redirect
from django.core.serializers import serialize
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .forms import PagoForm
from .models import Pago
from apps.notificaciones.models import Notificacion

class ListadoPago(ListView):
    model = Pago

    def get_queryset(self):
        return self.model.objects.filter(visibilidad = True)
    
    def get(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('pago:inicio_pago')
        

class CrearPago(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pago/crear_pago.html'

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_pago = Pago(
                    credito=form.cleaned_data.get('credito'),
                    monto_pagado=form.cleaned_data.get('monto_pagado'),
                    fecha_pago=form.cleaned_data.get('fecha_pago'),
                    estado_pago=form.cleaned_data.get('estado_pago'),
                    tipo_pago=form.cleaned_data.get('tipo_pago'),
                )
                nuevo_pago.save()
                Notificacion.objects.create(
                    mensaje=f'{self.model.__name__} registrado correctamente',
                    detalles=f'{self.model.__name__} {nuevo_pago.credito} registrado correctamente.'
                )
                mensaje = f'{self.model.__name__} registrado correctamente' 
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje , 'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar' 
                error = form.errors
                response = JsonResponse({'mensaje':mensaje , 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('pago:inicio_pago')

class ActualizarPago(UpdateView):
    model = Pago
    template_name = 'pago/editar_pago.html'
    form_class = PagoForm

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                # Crear notificación
                Notificacion.objects.create(
                    mensaje=f'{self.model.__name__} actualizado correctamente',
                    detalles=f'{self.model.__name__} {form.cleaned_data.get("credito")} actualizado correctamente.'
                )
                mensaje = f'{self.model.__name__} actualizado correctamente' 
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje , 'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar' 
                error = form.errors
                response = JsonResponse({'mensaje':mensaje , 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('pago:inicio_pago')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagos'] = Pago.objects.filter(visibilidad = True)
        return context

class EliminarPago(DeleteView):
    model = Pago
    template_name = 'pago/eliminar_pago.html'

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':   
            pago = self.get_object()
            pago.visibilidad = False
            pago.save()
            # Crear notificación
            Notificacion.objects.create(
                mensaje=f'{self.model.__name__} eliminado correctamente',
                detalles=f'{self.model.__name__} {pago.credito} eliminado correctamente.'
            )
            mensaje = f'{self.model.__name__} eliminado correctamente' 
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje , 'error':error})
            response.status_code = 200
            return response
        else:
            return redirect('pago:inicio_pago')
        

class AprobarPago(View):
    def post(self, request, *args, **kwargs):
        pago = get_object_or_404(Pago, pk=self.kwargs['pk'])
        pago.estado_pago = 'realizado'  # Ajusta según tu modelo
        pago.save()
        
        # Puedes agregar una notificación si lo deseas
        # Notificacion.objects.create(mensaje=f'Pago {pago.id} aprobado correctamente', detalles='Detalles...')
        
        return JsonResponse({'mensaje': 'Pago aprobado correctamente', 'error': None})
