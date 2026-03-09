from django.db import models


class Auto(models.Model):
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    año = models.IntegerField(verbose_name="Año")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"
        ordering = ['-año']

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
