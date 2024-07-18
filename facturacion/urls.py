from django.urls import path
app_name = 'fac'
from .views import ClienteList,ClienteCreateView,ClienteUpdateView,cliente_inactivar
urlpatterns = [
     
     path("clientes-lista/",ClienteList.as_view(), name="clientes-lista"),
     path("clientes-create/",ClienteCreateView.as_view(), name="crear-clientes"),
     path("clientes-create/<int:pk>/",ClienteUpdateView.as_view(), name="Update-clientes"),
     path("inactivar-cliente/<int:pk>/",cliente_inactivar,name="cliente-inactivo"),
     
]