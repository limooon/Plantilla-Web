from django.contrib import admin
from .models import Categorias,SubCategorias,Marca,UnidadMedida,Producto

# Registrar el modelo Categorias en el administrador

@admin.register(Categorias)
@admin.register(SubCategorias)
@admin.register(Marca)
@admin.register(UnidadMedida)


class CategoriasAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'fecha_creacion', 'fecha_modificacion']  # Campos a mostrar en la lista de categorías
    list_display_links = ['id', 'descripcion']  # Campos que enlazarán a la vista de detalle
    search_fields = ['descripcion']  # Campos por los cuales se puede buscar
    list_filter = ['fecha_creacion', 'fecha_modificacion']  # Filtros laterales
    ordering = ['-fecha_creacion']  # Ordenar por fecha de creación descendente
    
@admin.register(Producto) 
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'codigo', 'codigo_barra', 'precio', 'existencia', 'estado', 'fecha_creacion', 'fecha_modificacion']
    list_display_links = ['id', 'descripcion']
    search_fields = ['descripcion', 'codigo', 'codigo_barra']
    list_filter = ['estado', 'fecha_creacion', 'fecha_modificacion']
    ordering = ['-fecha_creacion']