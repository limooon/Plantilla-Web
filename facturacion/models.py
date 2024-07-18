from django.db import models
from core.models import ClaseModelo
from Inv.models import Producto

class Cliente(ClaseModelo):
    
    NAT= 'NATURAL'
    JUR='JURIDICA'
    
    TIPO_CLIENTE = [
        (NAT, 'NATURAL'),
        (JUR, 'JURIDICA'),
    ]
    
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    celular = models.CharField(max_length=10, blank=True, null=True)
    tipo = models.CharField(max_length=10, choices= TIPO_CLIENTE, default=NAT)


    def __str__(self):
        return '{}{}'.format(self.apellidos,self.nombres)

    def save(self, *args, **kwargs):
       self.nombres =self.nombres.upper()
       self.apellidos = self.apellidos.upper()
       super(Cliente, self).save(*args, **kwargs) 
       
    class Meta:
        verbose_name_plural = 'Clientes'
        
        
class Facturacion(ClaseModelo):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_total = models.DateField(auto_now_add=False)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    class Meta:
        verbose_name = "Encabezado de Factura"
        verbose_name_plural = "Encabezado de Facturas"

    def __str__(self):
        return '{}'.format(self.id)
    
    def save(self, *args, **kwargs):
       self.total =self.sub_total-self.descuento
       super(Facturacion, self).save(*args, **kwargs) 
    
    
class FacturacionDetalle(ClaseModelo):
    factura = models.ForeignKey(Facturacion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    dscuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    class Meta:
        verbose_name = "Detalle de Factura"
        verbose_name_plural = "Detalle de Facturas"

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self, *args, **kwargs):
       self.sub_total = float(float(int(self.cantidad)) * float(self.precio))
       self.total = self.sub_total - float(self.descuento)
       super(FacturacionDetalle, self).save(*args, **kwargs) 
