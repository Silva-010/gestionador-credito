from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateField(auto_now_add=True)  # Configura auto_now_add
    visibilidad = models.BooleanField('Visibilidad', default= True)

    def __str__(self):
        return f"{self.rut} | {self.nombres} {self.apellido_paterno}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['apellido_paterno']
