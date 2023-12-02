from django.db import models

class Banco(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    visibilidad = models.BooleanField('Visibilidad', default= True)

    def natural_key(self):
        return (self.nombre)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
        ordering = ['nombre']
