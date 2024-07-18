from django.db import models
from core.models import ClaseModelo
from Inv.models import Producto
# Create your models here.

class Provedor(ClaseModelo):
    descripcion = models.CharField(max_length=100, unique=True)
    direcion = models.CharField(max_length=250, null=True, blank=True)  # Permitimos null y blank para este campo
    contacto = models.CharField(max_length=250)
    telefono = models.CharField(max_length=10, null=True, blank=True)  # Permitimos null y blank para este campo
    email = models.EmailField(max_length=254, null=True, blank=True)
    
    
    def __str__(self):
            return '{}'.format(self.descripcion)
        
    def save(self):
            self.descripcion = self.descripcion.upper()
            super(Provedor, self).save()
        
    class Meta:
            verbose_name_plural = 'provedores'
    
    
class ComprasEncabezado(ClaseModelo):
    fecha_compra = models.DateField(null=True, blank=True)
    observacion = models.TextField(null=True, blank=True)
    no_factura = models.CharField(max_length=100)
    fecha_factura = models.DateField()
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    provedor = models.ForeignKey(Provedor, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.observacion

    def save(self, *args, **kwargs):
        self.observacion = self.observacion.upper()
        self.total = self.sub_total - self.descuento
        super(ComprasEncabezado, self).save(*args, **kwargs)
            
    class Meta:
        verbose_name = "Compra Encabezado"
        verbose_name_plural = "Compras Encabezados"

class ComprasDetalle(ClaseModelo):
    compra = models.ForeignKey(ComprasEncabezado,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio_prv = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    costo = models.FloatField(default=0)

    class Meta:
        verbose_name = "Compra Detalle"
        verbose_name_plural = "Compras Detalles"

    def __str__(self):
        return str(self.producto)

    def save(self, *args, **kwargs):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_prv))
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDetalle, self).save(*args, **kwargs)