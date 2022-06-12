from django.db import router
from django.urls import path
from django.urls.conf import include
from core.views import base, eliminar_producto, galeria, home, listado_productos, modificar_producto, nuevo_producto, contacto, registro_usuario

from .views import ProductoViewSet, agregar_producto, limpiar_carrito, restar_producto, tienda
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos',ProductoViewSet)

urlpatterns = [
    path('', home , name="home"),
    path('base/',base,name="base"),
    path('galeria/',galeria,name="galeria"),
    path('contacto/',contacto,name="contacto"),
    path('listado_productos/',listado_productos,name="listado_productos"),
    path('nuevo_producto/',nuevo_producto,name="nuevo_producto"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro_usuario, name="registro_usuario"),
    path('tienda/', tienda, name="tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('api/',include(router.urls)),
]
