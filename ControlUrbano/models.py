from django.db import models
from django.contrib.auth.models import User
from core.models import ClaseModelo
from django.core.validators import MaxValueValidator, MinValueValidator
 
class Catastro(ClaseModelo):
    
    URBANO = 'URBANO'
    RUSTICO = 'RUSTICO'
    RURAL = 'RURAL'

    TIPO_PREDIO = [
        (URBANO, 'URBANO'),
        (RUSTICO, 'RUSTICO'),
        (RURAL, 'RURAL'),
    ]

    SI = 'SI'
    NO = 'NO'

    TIPO_CONDOMINIO = [
        (SI, 'SI'),
        (NO, 'NO'),
    ]

    SI = 'SI'
    NO = 'NO'

    TIPO_FRENTE = [
        (SI, 'SI'),
        (NO, 'NO'),
    ]
    
    
    SI_S = 'SI'
    NO_S = 'NO'

    TIPO_USO_SUELO = [
        (SI_S, 'SI'),
        (NO_S, 'NO'),
    ]
    
    PERSONA_M = 'MORAL'
    PERSONA_F = 'FISICA'

    TIPO_PERSONA = [
        (PERSONA_M,'MORAL'),
        (PERSONA_F,'FISICA'),
    ]
    
    nombre_propietario = models.CharField(max_length=100)
    email = models.EmailField(default="s/n")
    telefono = models.CharField(max_length=20, default="s/n")
    direccion = models.CharField(max_length=255, default="s/n")
    representante_legal = models.CharField(max_length=100,blank=True)
    numero_oficial = models.CharField(max_length=8)
    clave_catastral = models.CharField(max_length=8)
    superficie = models.DecimalField(max_digits=10, decimal_places=2)
    calle = models.CharField(max_length=255,default="s/n")#select de vialidades
    numero_exterior = models.CharField(max_length=6,default="s/n")
    numero_interior = models.CharField(max_length=6,default="s/n",)
    colonia = models.CharField(max_length=100,default="s/n")#select de colinias
    delegacion = models.CharField(max_length=100,default="s/n")
    codigo_postal = models.CharField(max_length=5,default="s/n")
    manzana = models.CharField(max_length=3)
    lote = models.CharField(max_length=3)
    fracciones = models.CharField(max_length=50, blank=True, null=True)
    parcelas = models.CharField(max_length=50, blank=True, null=True)
    condominio = models.CharField(choices=TIPO_CONDOMINIO,default=NO)
    unidad = models.CharField(max_length=50, blank=True, null=True)
    nombre_condominio = models.CharField(max_length=100, blank=True, null=True)
    valor_unitario_zona = models.IntegerField(default=0)
    castigo = models.IntegerField(default=0)
    valor_unitario_predio = models.IntegerField(default=0)
    valor_unitario_provicional = models.IntegerField(default=0)
    superficie_construccion = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    uso_suelo = models.CharField(choices=TIPO_USO_SUELO,default=NO_S)
    tasa = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    frente_comun = models.CharField(choices= TIPO_FRENTE, default=NO)
    valor_fiscal = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    fecha_alta = models.DateTimeField()
    fecha_vigencia = models.DateField(blank=True, null=True)
    fecha_notificacion = models.DateField(blank=True, null=True)
    clave_anterior = models.CharField(max_length=8, blank=True, null=True)
    comentario = models.TextField(default="s/n")
    tipo = models.CharField(choices= TIPO_PREDIO, default=URBANO)
    minicipio = models.CharField(max_length=50, default="Ensenada")
    distrito = models.CharField(max_length=2, default="01")
    estado = models.CharField(max_length=50,default="Baja California Norte")
    pais = models.CharField(max_length=50,default="Mexico")
    sector = models.CharField(max_length=80,default="s/n")
    domicilio = models.CharField(max_length=180,default="s/n")
    tipo_persona = models.CharField(choices= TIPO_PERSONA, default=PERSONA_F)
    
    
    
    def save(self):
        self.nombre_propietario = self.nombre_propietario.upper()
        self.clave_catastral = self.clave_catastral.upper()
        self.representante_legal = self.representante_legal.upper()
        self.calle = self.calle.upper()
        self.comentario = self.comentario.upper()
        super(Catastro, self).save()
 
    def __str__(self):
        return f"Usuario Creación ID: {self.usuario_creacion_id} - Usuario Creación: {self.usuario_creacion.username}"

class Notificaciones(ClaseModelo):
    
    RA = "TIPOS DE VALORES"
    RA3 = 'RA3 - RECTIFICACION VALORES'
    RA4 = 'RA4 - RECTIFICACION NOMBRE'
    RA5 = 'RA5 - RECTIFICACION DIRECION'
    RA6 = 'RA6 - CAMBIO CLAVE'
    RA7 = 'RA7 - RECTIFICACION TASA'
    RA8 = 'RA8 - RECTIFICACION VIGENCIA'
    RA9 = 'RA9 - SITUACION LEGAL'
    RA10 ='RA10 - RECTIFICACION COLINDANCIAS'
    RA11 ='RA11 - RECTIFICACION ANTECEDENTE'
    

    TIPO_TRAMITE = [
        ( RA,'TIPOS DE VALORES'),
        ( RA3,'RA3 - RECTIFICACION VALORES'),
        ( RA4,'RA4 - RECTIFICACION NOMBRE'),
        ( RA5,'RA5 - RECTIFICACION DIRECION'),
        ( RA6,'RA6 - CAMBIO CLAVE'),
        ( RA7,'RA7 - RECTIFICACION TASA'),
        ( RA8,'RA8 - RECTIFICACION VIGENCIA'),
        ( RA9,'RA9 - SITUACION LEGAL'),
        ( RA10,'RA10 - RECTIFICACION COLINDANCIAS'),
        ( RA11,'RA11 - RECTIFICACION ANTECEDENTE'),
    ]
    
    datos = models.ForeignKey(Catastro,on_delete=models.CASCADE)
    colindancias = models.CharField(max_length=150, blank=True)
    rfc = models.CharField(max_length=13, blank=True)  
    curp = models.CharField(max_length=18, blank=True)  
    pensionado = models.BooleanField(default=False)
    nombre_casada = models.CharField(max_length=80, blank=True)
    observaciones = models.CharField(max_length=150, blank=True)
    opcion_tramite = models.CharField(choices= TIPO_TRAMITE, default=RA)
    numero_tramite = models.IntegerField(
        validators=[MinValueValidator(6)], default=000000
    )
    
    
    def __str__(self):
        return f"Notificación ID: {self.id} - {self.datos.nombre_propietario}"
   
    

