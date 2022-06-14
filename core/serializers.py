# SERIALIZADOR DE DJANGO: 
## bbdd - > datos  -> JSON
## JSON - > datos  -> bbdd

from rest_framework import serializers 
from .models import Producto

class ProductosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = ['nombre','valor','anio','categoria','descripcion']