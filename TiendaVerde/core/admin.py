from django.contrib import admin
from .models import Pedido, Producto

# Register your models here.

admin.site.register(Producto)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('name', 'cantidad', 'precio_total', 'estado', 'correo') 
    list_editable = ('estado',)