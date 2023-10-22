from django.shortcuts import redirect
from django.core.serializers import serialize
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.http import HttpResponse, JsonResponse
from .forms import SolicitudForm
from .models import SolicitudCredito

# Create your views here.

class ListadoSolicitud(ListView):
    model = SolicitudCredito

    def get_queryset(self):
        return self.model.objects.filter(visibilidad = True)
    
    def get(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('solicitud:inicio_solicitud')
        

class CrearSolicitud(CreateView):
    model = SolicitudCredito
    form_class = SolicitudForm
    template_name = 'solicitud/crear_solicitud.html'

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_solicitud = SolicitudCredito(
                    cliente=form.cleaned_data.get('cliente'),
                    banco=form.cleaned_data.get('banco'),
                    monto_solicitado=form.cleaned_data.get('monto_solicitado'),
                    fecha_solicitud=form.cleaned_data.get('fecha_solicitud'),
                    estado_solicitud=form.cleaned_data.get('estado_solicitud'),
                    fecha_aprobacion=form.cleaned_data.get('fecha_aprobacion'),
                    tipo_credito=form.cleaned_data.get('tipo_credito'),
                )
                nuevo_solicitud.save()
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
            return redirect('solicitud:inicio_solicitud')

class ActualizarSolicitud(UpdateView):
    model = SolicitudCredito
    template_name = 'solicitud/editar_solicitud.html'
    form_class = SolicitudForm

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
            return redirect('solicitud:inicio_solicitud')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solicitudes'] = SolicitudCredito.objects.filter(visibilidad = True)
        return context

class EliminarSolicitud(DeleteView):
    model = SolicitudCredito
    template_name = 'solicitud/eliminar_solicitud.html'

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
            return redirect('solicitud:inicio_solicitud')
