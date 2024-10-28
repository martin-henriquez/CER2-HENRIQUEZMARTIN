from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import login as ingresar, authenticate, logout
from core.models import Pedido, Producto
from core.carrito import Carrito

# Create your views here.
def home(request):    
    return render(request, 'core/base.html')

def inicio(request):
    return render(request, 'core/index.html')

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'core/catalogo.html', {'productos': productos})

def addProducto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.addProduct(producto)
    return redirect(to = 'catalogo')

def delProducto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.eliminar(producto)
    return redirect(to='catalogo')

def removeProducto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.quitar(producto)
    return redirect(to='catalogo')

def cleanCarrito(request):
    carrito = Carrito(request)
    carrito.cleanner()
    return redirect(to='catalogo')

def formulario(request):
    return render(request, 'core/formulario.html')

def login(request):
    return render(request, 'core/login.html')

def exit(request):
    logout(request)
    return redirect('inicio')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():            
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            ingresar(request, user)
            return redirect(to='inicio')
        
        data["form"] = user_creation_form
        
    return render(request, 'registration/register.html', data)

def envio_pedido(request):
    if request.method == 'POST':
        # Obtener los datos del carrito de la sesión
        carrito = request.session.get('carrito', {})
        correo_usuario = request.user.email # Obtener el usuario logueado
        
        # Recorrer los productos en el carrito y guardar cada uno como un Pedido
        for key, value in carrito.items():
            nombre_producto = value['nombre']
            cantidad = value['cantidad']
            precio_total = value['precio_total']
            
            
            # Crear una instancia del modelo Pedido y guardar en la base de datos
            pedido = Pedido(
                name = nombre_producto,
                cantidad=cantidad,
                precio_total = precio_total,
                estado = 'pendiente',
                correo = correo_usuario)
            
            carrito = Carrito(request)
            carrito.cleanner()
            pedido.save()
        return redirect('catalogo')  
    else:
    
        return redirect('core/catalogo')

