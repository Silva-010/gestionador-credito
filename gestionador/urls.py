"""
URL configuration for gestionador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login
from apps.cliente.views import Inicio
from apps.usuario.views import Login, logoutUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include(('apps.cliente.urls', 'cliente'))),
    path('banco/', include(('apps.banco.urls', 'banco'))),
    path('ejecutivo/', include(('apps.ejecutivo.urls', 'ejecutivo'))),
    path('solicitud/', include(('apps.solicitud.urls', 'solicitud'))),
    path('credito/', include(('apps.credito.urls', 'credito'))),
    path('pago/', include(('apps.pago.urls', 'pago'))),
    path('', login_required(Inicio.as_view()), name= 'index'),
    path('accounts/login/', Login.as_view(), name= 'login'),
    path('logout',login_required(logoutUser), name= 'logout'),
]
