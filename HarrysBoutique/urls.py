from django.contrib import admin
from django.urls import include, path

from core.views import agregar_producto, eliminar_producto, limpiar_carrito, restar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

admin.site.site_header = "Administración de Harry's Boutique"