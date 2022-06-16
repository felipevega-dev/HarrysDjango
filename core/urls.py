from django.urls import path, include
from core.views import  base, carrito, eliminar_producto, home, listado_productos, modificar_producto, nuevo_producto, contacto,\
    registro_usuario, cambiarpassword, perfil,tienda, ProductoViewSet, CategoriaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos',ProductoViewSet)
router.register('categoria',CategoriaViewSet)

urlpatterns = [
    path('', home , name="home"),
    path('base/',base,name="base"),
    path('contacto/',contacto,name="contacto"),
    path('listado_productos/',listado_productos,name="listado_productos"),
    path('nuevo_producto/',nuevo_producto,name="nuevo_producto"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro_usuario, name="registro_usuario"),
    path('tienda/', tienda, name="tienda"),
    path('api/', include(router.urls), name="api"),
    path('cambiarpassword/',cambiarpassword,name="cambiarpassword"),
    path('perfil/', perfil, name="perfil" ),
    path('carrito/', carrito, name="carrito"),
]
