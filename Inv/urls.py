
from django.urls import path
from .views import ProductoUpdateView,Producto_inactivar,ProductoCreateView,ProductoListView,UnidadMedidaListView,UnidadMedidaCreateView,UnidadMedidaUpdateView,um_inactivar,SubCategoriaUpdateView,SubCategoriaDeleteView,CreateViewSubCategorias,SubCategoriasList,CategoriaListView,CreateViewCategorias,CategoriaUpdateView,CategoriaDeleteView,MarcaList,MarcaCreateView,MarcaUpdateView,marca_inactivar
app_name = 'Inv'
urlpatterns = [
     
     path("categorias/", CategoriaListView.as_view(), name="categoria_lista"),
     path("add-categorias/", CreateViewCategorias.as_view(), name="categoria-add"),
     path("update-categorias/<int:pk>/", CategoriaUpdateView.as_view(), name="categoria-update"),
     path("delete-categorias/<int:pk>/", CategoriaDeleteView.as_view(), name="categoria-delete"),
     
     path("list-subcategorias/",SubCategoriasList.as_view(), name="subcategorias-list"),
     path("add-subcategorias/",CreateViewSubCategorias.as_view(), name="subcategorias-add"),
     path("update-subcategorias/<int:pk>/",SubCategoriaUpdateView.as_view(), name="subcategorias-update"),
     path("delete-subcategorias/<int:pk>/",SubCategoriaDeleteView.as_view(), name="subcategorias-delete"),
     
     path("list-marca/",MarcaList.as_view(), name="marca-list"),
     path("add-marca/",MarcaCreateView.as_view(), name="marca-add"),
     path("update-marca/<int:pk>/",MarcaUpdateView.as_view(), name="marca-update"),
     path("inactiv-marca/<int:pk>/",marca_inactivar, name="marca-inactiva"),
     
     path("list-medida/",UnidadMedidaListView.as_view(), name="medida-list"),
     path("add-um/",UnidadMedidaCreateView.as_view(), name="um-add"),
     path("update-um/<int:pk>/",UnidadMedidaUpdateView.as_view(), name="um-update"),
     path("inactiv-um/<int:pk>/",um_inactivar, name="um-inactiva"),
     
     path("list-productos/",ProductoListView.as_view(), name="producto-list"),
     path("add-producto/",ProductoCreateView.as_view(), name="producto-add"),
     path("update-producto/<int:pk>/",ProductoUpdateView.as_view(), name="producto-update"),
     path("inactiv-producto/<int:pk>/",Producto_inactivar, name="producto-inactiva"),
]