from django.contrib import admin
from .models import Producto, Categoria , Contacto
from .forms import ProductosForm

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','valor','anio','categoria']
    list_editable = ['valor']
    search_fields = ['nombre','anio']
    list_filter = ['categoria']
    list_per_page: 10

    form = ProductosForm
    
    
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)