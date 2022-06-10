from django.contrib import admin

from .models import Producto, Categoria

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','valor','anio','categoria']
    search_fields = ['nombre','anio']
    list_filter = ['categoria']
    list_per_page: 10
    
    
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)