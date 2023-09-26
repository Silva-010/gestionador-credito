from django.db import models
from apps.banco.models import Banco

class Ejecutivo(models.Model):
    id_banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

    class Meta:
        verbose_name = 'Ejecutivo'
        verbose_name_plural = 'Ejecutivos'
        ordering = ['id_banco']