from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import ListadoCliente, ActualizarCliente, EliminarCliente, CrearCliente

urlpatterns = [
    path('crear_cliente/', login_required(CrearCliente.as_view()), name= 'crear_cliente'),
    path('listar_cliente/', login_required(ListadoCliente.as_view()), name= 'listar_cliente'),
    path('editar_cliente/<int:pk>/', login_required(ActualizarCliente.as_view()), name= 'editar_cliente'),
    path('eliminar_cliente/<int:pk>/', login_required(EliminarCliente.as_view()), name= 'eliminar_cliente'),
]

#URLS DE VISTAS IMPLICITAS 

urlpatterns += [
    path('inicio_cliente/',login_required(
                                TemplateView.as_view(
                                    template_name = 'cliente/listar_cliente.html'
                                )), 
                            name= 'inicio_cliente'),
]
