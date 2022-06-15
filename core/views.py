from django.shortcuts import redirect,render , get_object_or_404
from core.carrito import Carrito
from core.forms import CustomUserForm, ProductosForm , ContactoForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from core.models import Categoria, Producto
from django.core.paginator import Paginator
from django.http import Http404

#REST
from rest_framework import viewsets
from .serializers import CategoriaSerializer, ProductosSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')
        descripcion = self.request.GET.get('descripcion')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)

        if descripcion:
            productos = productos.filter(descripcion__contains=descripcion)

        return productos   

# Create your views here.

def home(request):
    return render(request,'harrys/index.html')

def base(request):
    return render(request,'harrys/base.html')

@login_required
def perfil(request):
    return render(request,'registration/perfil.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tu Mensaje se ha enviado Correctamente")
            return redirect(to="contacto")
        else:
            data["form"] = formulario
            
    return render(request,'harrys/contacto.html', data)

@permission_required('core.view_producto')
def listado_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try: 
        paginator = Paginator(productos,5)
        productos = paginator.page(page)
    except:
        raise Http404

    data={
        'entity':productos,
        'paginator': paginator
    }

    return render(request,'harrys/listado_productos.html',data)

@permission_required('core.add_producto')
def nuevo_producto(request):
    data = {
        'form':ProductosForm()
    }
    
    if request.method == 'POST':
        formulario = ProductosForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Agregado Correctamente")
            return redirect(to="listado_productos")
        else:   
            data['form'] = formulario
        
    return render(request,'harrys/nuevo_producto.html',data)

@permission_required('core.change_producto')
def modificar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    data = {
        'form':ProductosForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Modificado Correctamente")
            return redirect(to="listado_productos")
        data['form'] = formulario 
          
    return render(request,'harrys/modificar_productos.html', data)

@permission_required('core.delete_producto')
def eliminar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request, "Producto Eliminado Correctamente")
    return redirect(to="listado_productos")
    
    # from django.shortcuts import render, redirect    


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
            user = authenticate(username=formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
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

def eliminar_producto_car(request, producto_id):
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


@login_required()
def cambiarpassword(request):
    form=PasswordChangeForm(request.POST or None)
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu Contraseña ha sido Modificada Correctamente")
            return redirect(to="perfil")
    
    return render(request,"app/cambiarpassword.html",contexto)

