from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import ListadoEjecutivo, ActualizarEjecutivo, EliminarEjecutivo, CrearEjecutivo

urlpatterns = [
    path('crear_ejecutivo/', login_required(CrearEjecutivo.as_view()), name= 'crear_ejecutivo'),
    path('listar_ejecutivo/', login_required(ListadoEjecutivo.as_view()), name= 'listar_ejecutivo'),
    path('editar_ejecutivo/<int:pk>/', login_required(ActualizarEjecutivo.as_view()), name= 'editar_ejecutivo'),
    path('eliminar_ejecutivo/<int:pk>/', login_required(EliminarEjecutivo.as_view()), name= 'eliminar_ejecutivo'),
]

#URLS DE VISTAS IMPLICITAS 

urlpatterns += [
    path('inicio_ejecutivo/',login_required(
                                TemplateView.as_view(
                                    template_name = 'ejecutivo/listar_ejecutivo.html'
                                )), 
                            name= 'inicio_ejecutivo'),
]
