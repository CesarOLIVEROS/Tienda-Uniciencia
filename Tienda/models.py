from django.db import models

from decimal import Decimal

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    correo=models.EmailField(unique=True)
    telefono=models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"