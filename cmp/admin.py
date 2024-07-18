from django.contrib import admin
from .models import Provedor, ComprasEncabezado, ComprasDetalle

# Register your models here.
admin.site.register(Provedor)
admin.site.register(ComprasEncabezado)
admin.site.register(ComprasDetalle)
