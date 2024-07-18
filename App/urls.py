
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('core.urls',namespace='core')),
    path('inv/', include('Inv.urls',namespace='inventario')),
    path('cmp/', include('cmp.urls',namespace='provedores')),
    path('facturacion/', include('facturacion.urls',namespace='facturacion')),
    path('control-urbano/', include('ControlUrbano.urls',namespace='ControlUrbano')),
    path('admin/', admin.site.urls),
]
