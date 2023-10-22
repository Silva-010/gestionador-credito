from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.cliente.models import Cliente
from apps.banco.models import Banco

class SolicitudCredito(models.Model):
    ESTADO_CHOICES = (
        ('en_espera', 'En Espera'),
        ('aprobado', 'Aprobado'),
        ('otros', 'Otros'),
    )

    TIPO_CREDITO_CHOICES = (
        ('credito_personal', 'Crédito Personal'),
        ('credito_hipotecario', 'Crédito Hipotecario'),
        ('credito_automotriz', 'Crédito Automotriz'),
        # Agrega más opciones según tus necesidades
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    monto_solicitado = models.IntegerField()
    fecha_solicitud = models.DateField()
    estado_solicitud = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='en_espera')
    fecha_aprobacion = models.DateField(blank=True, null=True)
    tipo_credito = models.CharField(max_length=20, choices=TIPO_CREDITO_CHOICES, default='credito_personal')
    visibilidad = models.BooleanField('Visibilidad', default= True)

    def __str__(self):
        return f"Solicitud de {self.cliente} a {self.banco}"

    class Meta:
        verbose_name = 'Solicitud de Credito'
        verbose_name_plural = 'Solicitudes de Credito'
        ordering = ['cliente']

# Función para actualizar la fecha de aprobación al cambiar el estado
@receiver(pre_save, sender=SolicitudCredito)
def actualizar_fecha_aprobacion(sender, instance, **kwargs):
    if instance.estado_solicitud == 'aprobado':
        instance.fecha_aprobacion = instance.fecha_solicitud
    else:
        instance.fecha_aprobacion = None
