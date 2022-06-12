from django.db import models
from django.db.models.deletion import CASCADE
from django.forms import DateField

# Create your models here.

class Categoria(models.Model):
    #id -- > numero autoincrementable , Django lo hace por nosotros
    nombre = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    valor = models.IntegerField()
    anio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    descripcion = models.TextField(null=True, blank=True)  
    fecha_publicacion = models.DateField()

    def __str__(self):
        return f'{self.nombre} -> {self.valor}'

