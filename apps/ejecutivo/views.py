from django.shortcuts import redirect
from django.core.serializers import serialize
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.http import HttpResponse, JsonResponse
from .forms import EjecutivoForm
from .models import Ejecutivo, Banco

# Create your views here.

class ListadoEjecutivo(ListView):
    model = Ejecutivo

    def get_queryset(self):
        return self.model.objects.filter(visibilidad = True)
    
    def get(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('ejecutivo:inicio_ejecutivo')
        

class CrearEjecutivo(CreateView):
    model = Ejecutivo
    form_class = EjecutivoForm
    template_name = 'ejecutivo/crear_ejecutivo.html'

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_ejecutivo = Ejecutivo(
                    id_banco=form.cleaned_data.get('id_banco'),
                    nombre=form.cleaned_data.get('nombre'),
                    apellido_paterno=form.cleaned_data.get('apellido_paterno'),
                    apellido_materno=form.cleaned_data.get('apellido_materno'),
                    email=form.cleaned_data.get('email'),
                    telefono=form.cleaned_data.get('telefono'),
                )
                nuevo_ejecutivo.save()
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
            return redirect('ejecutivo:inicio_ejecutivo')

class ActualizarEjecutivo(UpdateView):
    model = Ejecutivo
    template_name = 'ejecutivo/editar_ejecutivo.html'
    form_class = EjecutivoForm

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
            return redirect('ejecutivo:inicio_ejecutivo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ejecutivos'] = Ejecutivo.objects.filter(visibilidad = True)
        return context

class EliminarEjecutivo(DeleteView):
    model = Ejecutivo
    template_name = 'ejecutivo/eliminar_ejecutivo.html'

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
            return redirect('ejecutivo:inicio_ejecutivo')
