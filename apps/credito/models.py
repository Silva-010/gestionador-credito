from django.db import models
from apps.solicitud.models import SolicitudCredito

class Credito(models.Model):
    ESTADO_CHOICES = (
        ('activo', 'Activo'),
        ('pagado', 'Pagado'),
        ('vencido', 'Vencido'),
        ('otros', 'Otros'),
    )

    solicitud_credito = models.OneToOneField(SolicitudCredito, on_delete=models.CASCADE, limit_choices_to={'visibilidad': True, 'estado_solicitud': 'aprobado'})  # Agregar esta línea)
    monto = models.IntegerField()
    tasa_de_interes = models.DecimalField(max_digits=5, decimal_places=2)
    plazo_en_meses = models.IntegerField()
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    visibilidad = models.BooleanField('Visibilidad', default= True)
    fecha_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def natural_key(self):
        return f"Credito de {self.solicitud_credito.cliente} por {self.monto}"

    def __str__(self):
        return f"Credito de {self.solicitud_credito.cliente} por {self.monto}"

    class Meta:
        verbose_name = 'Credito'
        verbose_name_plural = 'Creditos'
        ordering = ['-fecha_registro', 'estado']