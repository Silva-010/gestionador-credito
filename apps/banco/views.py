from django.shortcuts import redirect
from django.core.serializers import serialize
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.http import HttpResponse, JsonResponse
from .forms import BancoForm
from .models import Banco

# Create your views here.

class ListadoBanco(ListView):
    model = Banco

    def get_queryset(self):
        return self.model.objects.filter(visibilidad = True)
    
    def get(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('banco:inicio_banco')
        

class CrearBanco(CreateView):
    model = Banco
    form_class = BancoForm
    template_name = 'banco/crear_banco.html'

    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_banco = Banco(
                    nombre=form.cleaned_data.get('nombre'),
                    direccion=form.cleaned_data.get(''),
                    telefono=form.cleaned_data.get('telefono'),
                )
                nuevo_banco.save()
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
            return redirect('banco:inicio_banco')

class ActualizarBanco(UpdateView):
    model = Banco
    template_name = 'banco/editar_banco.html'
    form_class = BancoForm

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
            return redirect('banco:inicio_banco')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bancos'] = Banco.objects.filter(visibilidad = True)
        return context

class EliminarBanco(DeleteView):
    model = Banco
    template_name = 'banco/eliminar_banco.html'

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
            return redirect('banco:inicio_banco')
