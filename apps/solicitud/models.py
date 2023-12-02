from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from apps.cliente.models import Cliente
from apps.banco.models import Banco

class SolicitudCredito(models.Model):
    ESTADO_CHOICES = (
        ('espera', 'En Espera'),
        ('aprobado', 'Aprobado'),
        ('rechazada', 'Rechazada'),
        ('otros', 'Otros'),
    )

    TIPO_CREDITO_CHOICES = (
        ('consumo', 'Crédito de Consumo'),
        ('hipotecario', 'Crédito Hipotecario'),
        ('automotriz', 'Crédito Automotriz'),
        # Agrega más opciones según tus necesidades
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, limit_choices_to={'visibilidad': True})
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, limit_choices_to={'visibilidad': True})
    monto_solicitado = models.IntegerField()
    fecha_solicitud = models.DateField()
    estado_solicitud = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='en_espera')
    fecha_aprobacion = models.DateField(blank=True, null=True)
    tipo_credito = models.CharField(max_length=20, choices=TIPO_CREDITO_CHOICES, default='credito_personal')
    visibilidad = models.BooleanField('Visibilidad', default= True)
    fecha_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def natural_key(self):
        return f"Solicitud de {self.cliente} | {self.estado_solicitud}"

    def __str__(self):
        return f"Solicitud de {self.cliente} a {self.banco}"

    class Meta:
        verbose_name = 'Solicitud de Credito'
        verbose_name_plural = 'Solicitudes de Credito'
        ordering = ['-fecha_registro','cliente']

@receiver(pre_save, sender=SolicitudCredito)
def actualizar_fecha_aprobacion(sender, instance, **kwargs):
    if instance.estado_solicitud == 'aprobado':
        instance.fecha_aprobacion = timezone.now()
    else:
        instance.fecha_aprobacion = '0000-00-00'
