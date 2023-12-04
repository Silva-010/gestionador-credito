from django.core.paginator import Paginator
from django.views.generic import TemplateView
from apps.cliente.models import Cliente
from apps.solicitud import models
from django.db.models.functions import Cast
from apps.solicitud.models import SolicitudCredito
from apps.credito.models import Credito
from apps.pago.models import Pago
from apps.notificaciones.models import Notificacion
from django.db.models import Count, Sum, IntegerField, CharField, Func

class Inicio(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Recuentos
        context['recuento_clientes_activos'] = Cliente.objects.filter(visibilidad=True).count()
        context['recuento_solicitudes_activas'] = SolicitudCredito.objects.filter(visibilidad=True).count()
        context['recuento_creditos_aprobados'] = Credito.objects.filter(visibilidad=True).count()
        context['recuento_pagos'] = Pago.objects.filter(visibilidad=True).count()
        context['recuento_solicitudes_espera'] = SolicitudCredito.objects.filter(visibilidad=True,estado_solicitud='espera').count()
        context['recuento_solicitudes_aprobadas'] = SolicitudCredito.objects.filter(visibilidad=True,estado_solicitud='aprobado').count()
        context['recuento_solicitudes_rechazadas'] = SolicitudCredito.objects.filter(visibilidad=True,estado_solicitud='rechazada').count()
        context['recuento_solicitudes_otros'] = SolicitudCredito.objects.filter(visibilidad=True,estado_solicitud='otros').count()

        # Obtén el total de créditos
        total_creditos = Credito.objects.filter(visibilidad=True).count()
        # Calcula el porcentaje de cada tipo de crédito
        porcentaje_activos = (Credito.objects.filter(visibilidad=True, estado='activo').count() / total_creditos) * 100
        porcentaje_pagados = (Credito.objects.filter(visibilidad=True, estado='pagado').count() / total_creditos) * 100
        porcentaje_vencidos = (Credito.objects.filter(visibilidad=True, estado='vencido').count() / total_creditos) * 100
        # Agrega los porcentajes al contexto
        context['porcentaje_creditos_activos'] = round(porcentaje_activos, 2)
        context['porcentaje_creditos_pagados'] = round(porcentaje_pagados, 2)
        context['porcentaje_creditos_vencidos'] = round(porcentaje_vencidos, 2)
        
       # MontosSolicitados
        context['monto_solicitado_consumo'] = SolicitudCredito.objects.filter(visibilidad=True, tipo_credito='consumo') \
            .annotate(monto_solicitado_int=Cast(LimpiarMonto('monto_solicitado'), IntegerField())) \
            .aggregate(Sum('monto_solicitado_int'))['monto_solicitado_int__sum'] or 0

        context['monto_solicitado_hipotecario'] = SolicitudCredito.objects.filter(visibilidad=True, tipo_credito='hipotecario') \
            .annotate(monto_solicitado_int=Cast(LimpiarMonto('monto_solicitado'), IntegerField())) \
            .aggregate(Sum('monto_solicitado_int'))['monto_solicitado_int__sum'] or 0

        context['monto_solicitado_automotriz'] = SolicitudCredito.objects.filter(visibilidad=True, tipo_credito='automotriz') \
            .annotate(monto_solicitado_int=Cast(LimpiarMonto('monto_solicitado'), IntegerField())) \
            .aggregate(Sum('monto_solicitado_int'))['monto_solicitado_int__sum'] or 0

        # Notificaciones
        context['notificaciones'] = Notificacion.objects.all().order_by('-fecha_creacion')[:5]

        
        # Obtén todos los pagos con estado_pago = 'pendiente' para el to-do list
        pagos_pendientes = Pago.objects.filter(visibilidad=True, estado_pago='pendiente')
        # Número de pagos por página
        pagos_por_pagina = 6
        paginator = Paginator(pagos_pendientes, pagos_por_pagina)
        # Obtén el número de página desde la solicitud GET
        page = self.request.GET.get('page')
        # Obtén los pagos para la página actual
        pagos_en_pagina = paginator.get_page(page)
        context['pagos_pendientes'] = pagos_en_pagina
        
        return context
    
class LimpiarMonto(Func):
    function = 'regexp_replace'
    template = "%(function)s(%(expressions)s, '[^0-9]', '', 'g')"
    output_field = CharField()

def obtener_notificaciones():
    # Puedes ajustar esta lógica según tus necesidades
    # Aquí asumiré que tienes un modelo Notificacion con un campo mensaje
    # Asegúrate de importar el modelo y ajustar los nombres según sea necesario
    from apps.notificaciones.models import Notificacion
    notificaciones = Notificacion.objects.all().values('mensaje')
    return list(notificaciones)