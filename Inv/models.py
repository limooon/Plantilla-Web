from django.db import models
from core.models import ClaseModelo

class Categorias(ClaseModelo):
    descripcion = models.CharField('descripcion', max_length=100, help_text="descripcion", unique=True)
    
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(Categorias, self).save(*args, **kwargs)
    
    class Meta:
        
        verbose_name = 'Categoria'
        

        

class SubCategorias(ClaseModelo):
   categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE,default=1)
   descripcion = models.CharField('descripcion-sub', max_length=100, help_text="descripcion subcategoria")
   
   def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)
   
   def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategorias, self).save()
        
   class Meta:
        verbose_name = 'SubCategoria'
        verbose_name_plural = 'SubCategorias'
        unique_together = ('categoria','descripcion')
        
        
        
        


class Marca(ClaseModelo):
    descripcion = models.CharField('descripcion-marca', max_length=100, help_text="descripcion marca",unique=True)
    
    def __str__(self):
            return '{}'.format(self.descripcion)
        
    def save(self):
            self.descripcion = self.descripcion.upper()
            super(Marca, self).save()
        
    class Meta:
            verbose_name = 'marca'
            verbose_name_plural = 'marca'
            
            
class UnidadMedida(ClaseModelo):
    descripcion = models.CharField('unidad de medida', max_length=100, help_text="descripcion marca",unique=True)
    
    def __str__(self):
            return '{}'.format(self.descripcion)
        
    def save(self):
            self.descripcion = self.descripcion.upper()
            super(UnidadMedida, self).save()
        
    class Meta:
            verbose_name = 'unidad de medida'
            verbose_name_plural = 'unidades de medida'
        
            
class Producto(ClaseModelo):
    codigo = models.CharField('codigo', max_length=20, unique=True, default=None)
    codigo_barra = models.CharField('codigo barra', max_length=50, default=None)
    descripcion = models.CharField('descripcion', max_length=200, default=None)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)  # Ajusta a null=True, blank=True si permites nulos
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, null=True, blank=True)  # Ajusta a null=True, blank=True si permites nulos
    subcategoria = models.ForeignKey(SubCategorias, on_delete=models.CASCADE, null=True, blank=True)  # Ajusta a null=True, blank=True si permites nulos
    
    def __str__(self):
        return self.descripcion
    
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Productos'
        unique_together = ('codigo', 'codigo_barra')
        
        