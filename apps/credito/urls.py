from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import ListadoCredito, ActualizarCredito, EliminarCredito, CrearCredito

urlpatterns = [
    path('crear_credito/', login_required(CrearCredito.as_view()), name= 'crear_credito'),
    path('listar_credito/', login_required(ListadoCredito.as_view()), name= 'listar_credito'),
    path('editar_credito/<int:pk>/', login_required(ActualizarCredito.as_view()), name= 'editar_credito'),
    path('eliminar_credito/<int:pk>/', login_required(EliminarCredito.as_view()), name= 'eliminar_credito'),
]

#URLS DE VISTAS IMPLICITAS 

urlpatterns += [
    path('inicio_credito/',login_required(
                                TemplateView.as_view(
                                    template_name = 'credito/listar_credito.html'
                                )), 
                            name= 'inicio_credito'),
]
