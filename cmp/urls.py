from django.urls import path
from .views import productoslist,detalles_y_productos,Producto_inactivar,ComprasDetalleDeleteView,ComprasDetalleUpdateView,ComprasDetalleCreateView,ComprasDetalleListView,ComprasView, CreateViewCompras, ComprasUpdateView, ComprasDeleteView, ProvedorList, ProvedorCreateView, ProvedorUpdateView,provedor_inactivar
from .reportes import render_pdf_view,imprimir_compras
app_name = 'cmp' 

urlpatterns = [
    path('provedores/', ProvedorList.as_view(), name='provedor_list'),
    path('provedores/nuevo/', ProvedorCreateView.as_view(), name='provedor_create'),
    path('provedores/<int:pk>/editar/', ProvedorUpdateView.as_view(), name='provedor_update'),
    path('provedores/<int:pk>/inactivar/', provedor_inactivar, name='provedor_inactivar'),
    
    path('compras/', ComprasView.as_view(), name='compras_list'),
    path('compras/nuevo/', CreateViewCompras.as_view(), name='compras_create'),
    path('compras/editar/<int:pk>/', ComprasUpdateView.as_view(), name='compras_update'),
    path('compras/eliminar/<int:pk>/', ComprasDeleteView.as_view(), name='compras_delete'),
    #detalles de compras
    path('compras-detail/',ComprasDetalleListView.as_view(), name='compras_detalle'),
    path('compras-detalle/agregar/', ComprasDetalleCreateView.as_view(), name='compras_detalle_agregar'),
    path('compras-detalle/editar/<int:pk>/', ComprasDetalleUpdateView.as_view(), name='compras_detalle_editar'),
    path('compras-detalle/eliminar/<int:pk>/', ComprasDetalleDeleteView.as_view(), name='compras_detalle_delete'),
    
    #path('productos-disponibles/',ProductoDetalleListView.as_view(), name='productos-disponibles'),
    path("inactiv-producto/<int:pk>/",Producto_inactivar,name="producto-inactiva"),
    path('detalles-y-productos/',detalles_y_productos, name='detalles_y_productos'),
    path('productos/',productoslist, name='productoslist'),
    
    #imprimor
    path('comras-detalle/',render_pdf_view, name='render_pdf_view'),
    path('compra-id/<int:pk>/imprimir',imprimir_compras, name='imprimir_compras'),
]

