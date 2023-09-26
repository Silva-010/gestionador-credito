from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ClienteForm
from .models import Cliente
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoCliente(ListView):
    model = Cliente
    template_name = 'cliente/listar_cliente.html'
    context_object_name = 'clientes'
    queryset = Cliente.objects.filter(visibilidad = True)

class ActualizarCliente(UpdateView):
    model = Cliente
    template_name = 'cliente/crear_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:listar_cliente')

class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear_cliente.html'
    success_url = reverse_lazy('cliente:listar_cliente')

class EliminarCliente(DeleteView):
    model = Cliente
    
    def post(self, request, pk, *args, **kwargs):
        object = Cliente.objects.get(id = pk)
        object.visibilidad = False
        object.save()
        return redirect('cliente:listar_cliente')


def crearCliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('index')
    else:
        cliente_form = ClienteForm()
    return render(request, 'cliente/crear_cliente.html', {'cliente_form' : cliente_form})

def listarCliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/listar_cliente.html', {'clientes' : clientes})

def editarCliente(request, id):
    cliente_form = None
    error = None
    try:
        cliente = Cliente.objects.get(id = id)
        if request.method == 'GET':
            cliente_form = ClienteForm(instance = cliente)
        else:
            cliente_form = ClienteForm(request.POST, instance = cliente)
            if cliente_form.is_valid():
                cliente_form.save()
            return redirect('cliente:listar_cliente')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'cliente/crear_cliente.html', {'cliente_form' : cliente_form, 'error' : error}) 

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente:listar_cliente')
    return render(request, 'cliente/eliminar_cliente.html', {'cliente' : cliente})