"""
URL configuration for TiendaVerde project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin 
from core.views import addProducto, cleanCarrito, delProducto, envio_pedido, home, catalogo, exit, register, inicio, removeProducto

urlpatterns = [
    path('', home, name='home'),
    path('catalogo/', catalogo, name = 'catalogo'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('inicio/', inicio, name='inicio'),
    path("pedidos/", envio_pedido, name="pedidos"),
    
    path('agregar/<int:producto_id>/', addProducto, name='Add'),
    path('eliminar/<int:producto_id>/', delProducto, name='Del'),
    path('restar/<int:producto_id>/', removeProducto, name="Sub"),
    path('clanner/', cleanCarrito, name="CLS"),

]