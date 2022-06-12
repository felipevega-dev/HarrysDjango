from django.shortcuts import redirect,render , HttpResponse
from core.carrito import Carrito
from core.forms import CustomUserForm, ProductosForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from core.models import Producto

#REST
from rest_framework import viewsets
from .serializers import ProductosSerializer

# Create your views here.
def home(request):
    return render(request,'harrys/index.html')

def base(request):
    return render(request,'harrys/base.html')

def galeria(request):
    return render(request,'harrys/galeria.html')

def contacto(request):
    return render(request,'harrys/contacto.html')

def listado_productos(request):
    productos = Producto.objects.all()
    data={
        'productos':productos
    }
    return render(request,'harrys/listado_productos.html',data)

@permission_required('core.add_producto')
def nuevo_producto(request):
    data = {
        'form':ProductosForm()
    }
    
    if request.method == 'POST':
        formulario = ProductosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
        data['form'] = formulario
        
    return render(request,'harrys/nuevo_producto.html',data)

@login_required
def modificar_producto(request):
    producto = ProductosForm.objects.get(id=id)
    data = {
        'form':ProductosForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Producto Modificado Correctamente"
        data['form'] = formulario 
          
    return render(request,'harrys/modificar_producto.html', data)

def eliminar_producto(request):
    producto = Producto.objects.get(id=id)
    producto.delete()
    
    # from django.shortcuts import render, redirect    
    return render(request,'harrys/nuevo_producto.html')

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save();
            # autenticar al usuario y redirigir al inicio
            # debemos importar
            # from django.contrib.auth import login, authenticate
            # obtener la data del formulario
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password= password)
            login(request, user)
            return redirect(to='home')
        
    return render(request,"registration/registro.html",data)

#TIENDA

def tienda(request):
    productos = Producto.objects.all()
    return render(request,'harrys/tienda.html', {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id) 
    carrito.agregar(producto)
    return redirect("tienda")  

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id) 
    carrito.eliminar(producto)
    return redirect("tienda")  

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id) 
    carrito.restar(producto)
    return redirect("tienda") 

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")  


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

