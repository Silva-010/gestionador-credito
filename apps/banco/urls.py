from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import ListadoBanco, ActualizarBanco, EliminarBanco, CrearBanco

urlpatterns = [
    path('crear_banco/', login_required(CrearBanco.as_view()), name= 'crear_banco'),
    path('listar_banco/', login_required(ListadoBanco.as_view()), name= 'listar_banco'),
    path('editar_banco/<int:pk>/', login_required(ActualizarBanco.as_view()), name= 'editar_banco'),
    path('eliminar_banco/<int:pk>/', login_required(EliminarBanco.as_view()), name= 'eliminar_banco'),
]

#URLS DE VISTAS IMPLICITAS 

urlpatterns += [
    path('inicio_banco/',login_required(
                                TemplateView.as_view(
                                    template_name = 'banco/listar_banco.html'
                                )), 
                            name= 'inicio_banco'),
]
