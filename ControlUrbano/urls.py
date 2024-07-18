from django.urls import path
from .views import ( 
            Notificaion,
            CatastroDetailView,
            CatastroList,
            CatastroCreateView,
            CatastroUpdateView,
            CatastroDeleteView,
            NotificacionesList,
            NotificacionesCreateView,
            NotificacionesUpdateView,
            NotificacionesDeleteView,  
            NotificacionesDetailView,     
             
)  
  
from .reportes import render_pdf_view,notificacion_pdf_view
app_name = 'ControlUrbano' 

urlpatterns = [
    path('lista-registros/',CatastroList.as_view(), name='registros_lista'),
    path('add-registros/', CatastroCreateView.as_view(), name='registros_add'),
    path('update-registros/<int:pk>/', CatastroUpdateView.as_view(), name='registros_update'),
    path('delete-registros/<int:pk>/', CatastroDeleteView.as_view(), name='registros_delete'),
    path('detalle-registro/<int:pk>/', CatastroDetailView.as_view(), name='registros_detalle'),
    path('predios-detalle-pdf/<int:pk>',render_pdf_view, name='render_pdf_view'),
    #notificacion
    path('notificacion/',Notificaion.as_view(), name='notificacion'),
    path('lista-notificaciones/', NotificacionesList.as_view(), name='notificaciones_lista'),
    path('crear-notificacion/', NotificacionesCreateView.as_view(), name='notificacion_crear'),
    path('editar-notificacion/<int:pk>/', NotificacionesUpdateView.as_view(), name='notificacion_editar'),
    path('eliminar-notificacion/<int:pk>/', NotificacionesDeleteView.as_view(), name='notificacion_eliminar'),
    path('detalle-notificacion/<int:pk>/',  NotificacionesDetailView.as_view(), name='notificacion_detalle'),
    path('notificacion-detalle-pdf/<int:pk>',notificacion_pdf_view, name='notificacion_pdf_view'),
    
]