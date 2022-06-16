from django.shortcuts import render

from pedidos.models import Pedido

# Create your views here.
def nuevo_pedido(request):
    data = {
        Pedido()
    }
