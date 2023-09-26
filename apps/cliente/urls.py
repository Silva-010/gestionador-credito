from django.urls import path
from .views import crearCliente, listarCliente, editarCliente, eliminarCliente, ListadoCliente, ActualizarCliente, CrearCliente, EliminarCliente

urlpatterns = [
    path('crear_cliente/', CrearCliente.as_view(), name= 'crear_cliente'),
    path('listar_cliente/', ListadoCliente.as_view(), name= 'listar_cliente'),
    path('editar_cliente/<int:pk>', ActualizarCliente.as_view(), name= 'editar_cliente'),
    path('eliminar_cliente/<int:pk>', EliminarCliente.as_view(), name= 'eliminar_cliente'),
]
