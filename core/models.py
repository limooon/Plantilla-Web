from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ClaseModelo(models.Model):

    estado = models.BooleanField('estado', default=True)
    fecha_creacion = models.DateTimeField('fecha-creacion',auto_now_add=True)
    fecha_modificacion = models.DateTimeField('fecha-modificacion', auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.IntegerField(blank=True, null=True)
    
    class Meta:
        abstract = True