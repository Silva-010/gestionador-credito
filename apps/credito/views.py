from django.shortcuts import redirect
from django.core.serializers import serialize
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.http import HttpResponse, JsonResponse
from .forms import CreditoForm
from .models import Credito

class ListadoCredito(ListView):
    model = Credito

    def get_queryset(self):
        return self.model.objects.filter(visibilidad = True)
    
    def get(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('credito:inicio_credito')
        

class CrearCredito(CreateView):
    model = Credito
    form_class = CreditoForm
    template_name = 'credito/crear_credito.html'

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_credito = Credito(
                    solicitud_credito=form.cleaned_data.get('solicitud_credito'),
                    monto=form.cleaned_data.get('monto'),
                    tasa_de_interes=form.cleaned_data.get('tasa_de_interes'),
                    plazo_en_meses=form.cleaned_data.get('plazo_en_meses'),
                    fecha_creacion=form.cleaned_data.get('fecha_creacion'),
                    estado=form.cleaned_data.get('estado'),
                )
                nuevo_credito.save()
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
            return redirect('credito:inicio_credito')

class ActualizarCredito(UpdateView):
    model = Credito
    template_name = 'credito/editar_credito.html'
    form_class = CreditoForm

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
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
            return redirect('credito:inicio_credito')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creditos'] = Credito.objects.filter(visibilidad = True)
        return context

class EliminarCredito(DeleteView):
    model = Credito
    template_name = 'credito/eliminar_credito.html'

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':   
            cliente = self.get_object()
            cliente.visibilidad = False
            cliente.save()
            mensaje = f'{self.model.__name__} eliminado correctamente' 
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje , 'error':error})
            response.status_code = 200
            return response
        else:
            return redirect('credito:inicio_credito')
