from django.contrib import admin

from pedidos.models import LineaPedido, Pedido

# Register your models here.
admin.site.register([Pedido,LineaPedido])