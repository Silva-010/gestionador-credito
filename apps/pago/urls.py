from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import ListadoPago, ActualizarPago, EliminarPago, CrearPago, AprobarPago

urlpatterns = [
    path('crear_pago/', login_required(CrearPago.as_view()), name= 'crear_pago'),
    path('listar_pago/', login_required(ListadoPago.as_view()), name= 'listar_pago'),
    path('editar_pago/<int:pk>/', login_required(ActualizarPago.as_view()), name= 'editar_pago'),
    path('eliminar_pago/<int:pk>/', login_required(EliminarPago.as_view()), name= 'eliminar_pago'),
    path('aprobar_pago/<int:pk>/', AprobarPago.as_view(), name='aprobar_pago'),
]

#URLS DE VISTAS IMPLICITAS 

urlpatterns += [
    path('inicio_pago/',login_required(
                                TemplateView.as_view(
                                    template_name = 'pago/listar_pago.html'
                                )), 
                            name= 'inicio_pago'),
]
