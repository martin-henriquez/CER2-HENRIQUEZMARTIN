from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    
class Pedido(models.Model):
    
    name = models.CharField(max_length=64, null=True)  
    cantidad = models.PositiveIntegerField(default=1)  
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)  
    estado = models.CharField(max_length=10, default='pendiente', choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')]) 
    correo = models.EmailField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.cantidad} unidades de {self.name} - Total: {self.precio_total}"    