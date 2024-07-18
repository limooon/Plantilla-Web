from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'celular', 'tipo')
    list_filter = ('tipo', )
    search_fields = ('nombres', 'apellidos', 'celular')
    ordering = ('apellidos', 'nombres')
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombres', 'apellidos', 'celular')
        }),
        ('Tipo de Cliente', {
            'fields': ('tipo', )
        }),
        ('Fechas importantes', {
            'fields': ('fecha_creacion', 'fecha_modificacion'),
            'classes': ('collapse', )
        })
    )
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    date_hierarchy = 'fecha_creacion'

    def save_model(self, request, obj, form, change):
        if not change:  # Nuevo objeto
            obj.creado_por = request.user
        else:  # Objeto existente
            obj.modificado_por = request.user
        super().save_model(request, obj, form, change)
