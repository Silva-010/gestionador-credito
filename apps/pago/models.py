from django.db import models
from apps.credito.models import Credito

class Pago(models.Model):
    ESTADO_PAGO_CHOICES = (
        ('realizado', 'Realizado'),
        ('atrasado', 'Atrasado'),
        ('otros', 'Otros'),
    )

    TIPO_PAGO_CHOICES = (
        ('principal', 'Principal'),
        ('interes', 'Interés'),
        ('otros', 'Otros'),
    )

    credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    estado_pago = models.CharField(max_length=20, choices=ESTADO_PAGO_CHOICES, default='realizado')
    tipo_pago = models.CharField(max_length=20, choices=TIPO_PAGO_CHOICES, default='principal')
    visibilidad = models.BooleanField('Visibilidad', default= True)

    def __str__(self):
        return f"Pago de {self.monto_pagado} para {self.credito}"

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['fecha_pago']