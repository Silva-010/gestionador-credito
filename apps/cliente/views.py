from django.shortcuts import redirect
from django.core.serializers import serialize
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.http import HttpResponse, JsonResponse
from .forms import ClienteForm
from .models import Cliente
from apps.notificaciones.models import Notificacion

class ListadoCliente(ListView):
    model = Cliente 

    def get_queryset(self):
        return self.model.objects.filter(visibilidad = True)
    
    def get(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('cliente:inicio_cliente')
        

class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear_cliente.html'

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_cliente = Cliente(
                    rut=form.cleaned_data.get('rut'),
                    nombres=form.cleaned_data.get('nombres'),
                    apellido_paterno=form.cleaned_data.get('apellido_paterno'),
                    apellido_materno=form.cleaned_data.get('apellido_materno'),
                    email=form.cleaned_data.get('email'),
                    telefono=form.cleaned_data.get('telefono'),
                    direccion=form.cleaned_data.get('direccion'),
                )
                nuevo_cliente.save()
                Notificacion.objects.create(
                    mensaje=f'{self.model.__name__} registrado correctamente',
                    detalles=f'{self.model.__name__} {nuevo_cliente.nombres} {nuevo_cliente.apellido_paterno} registrado correctamente.'
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
            return redirect('cliente:inicio_cliente')
        
        

class ActualizarCliente(UpdateView):
    model = Cliente
    template_name = 'cliente/editar_cliente.html'
    form_class = ClienteForm

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                # Crear notificación
                Notificacion.objects.create(
                    mensaje=f'{self.model.__name__} actualizado correctamente',
                    detalles=f'{self.model.__name__} {form.cleaned_data.get("nombres")} {form.cleaned_data.get("apellido_paterno")} actualizado correctamente.'
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
            return redirect('cliente:inicio_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.filter(visibilidad = True)
        return context

class EliminarCliente(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar_cliente.html'

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':   
            cliente = self.get_object()
            cliente.visibilidad = False
            cliente.save()
            # Crear notificación
            Notificacion.objects.create(
                mensaje=f'{self.model.__name__} eliminado correctamente',
                detalles=f'{self.model.__name__} {cliente.nombres} {cliente.apellido_paterno} eliminado correctamente.'
            )
            mensaje = f'{self.model.__name__} eliminado correctamente' 
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje , 'error':error})
            response.status_code = 200
            return response
        else:
            return redirect('cliente:inicio_cliente')
