from django.contrib import admin
from .models import Catastro,Notificaciones


@admin.register(Catastro)
class CatastroAdmin(admin.ModelAdmin):
    list_display = ('clave_catastral', 'nombre_propietario', 'superficie', 'fecha_alta')
    list_filter = ('fecha_alta', 'tipo', 'condominio')
    search_fields = ('clave_catastral', 'nombre_propietario', 'codigo_postal')
    date_hierarchy = 'fecha_alta'
    list_per_page = 20  # Número de registros por página en la lista
    ordering = ('-fecha_alta',)  # Ordenar por fecha de alta descendente


@admin.register(Notificaciones)
class NotificacionesAdmin(admin.ModelAdmin):
    list_display = ('datos', 'colindancias', 'rfc', 'curp', 'pensionado', 'nombre_casada', 'observaciones')
    list_filter = ('pensionado',)  # Ejemplo de filtro
    search_fields = ('datos__clave_catastral', 'datos__nombre_propietario')
    list_per_page = 20
    ordering = ('-id',)  # Puedes ordenar por cualquier campo

    def datos(self, obj):
        return f'{obj.datos.clave_catastral} - {obj.datos.nombre_propietario}'

