from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import ListadoSolicitud, ActualizarSolicitud, EliminarSolicitud, CrearSolicitud

urlpatterns = [
    path('crear_solicitud/', login_required(CrearSolicitud.as_view()), name= 'crear_solicitud'),
    path('listar_solicitud/', login_required(ListadoSolicitud.as_view()), name= 'listar_solicitud'),
    path('editar_solicitud/<int:pk>/', login_required(ActualizarSolicitud.as_view()), name= 'editar_solicitud'),
    path('eliminar_solicitud/<int:pk>/', login_required(EliminarSolicitud.as_view()), name= 'eliminar_solicitud'),
]

#URLS DE VISTAS IMPLICITAS 

urlpatterns += [
    path('inicio_solicitud/',login_required(
                                TemplateView.as_view(
                                    template_name = 'solicitud/listar_solicitud.html'
                                )), 
                            name= 'inicio_solicitud'),
]
