# SERIALIZADOR DE DJANGO: 
## bbdd - > datos  -> JSON
## JSON - > datos  -> bbdd

from unittest.util import _MAX_LENGTH
from rest_framework import serializers 
from .models import Categoria, Producto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source="categoria.nombre")
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(),source="categoria")
    nombre = serializers.CharField(required=True, min_length=5)

    def validate_nombre(self,value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Este producto ya existe")

        return value    

    class Meta:
        model = Producto
        fields = '__all__'