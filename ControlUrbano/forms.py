
from django import forms
#from core.models import ClaseModelo
from django.contrib.auth.models import User
from .models import Catastro,Notificaciones

class CatastroForm(forms.ModelForm):
    class Meta:
        model = Catastro
        fields = [
            'nombre_propietario',
            'email',
            'telefono',
            'direccion',
            'representante_legal',
            'numero_oficial',
            'clave_catastral',
            'superficie',
            'calle',
            'numero_exterior',
            'numero_interior',
            'colonia',
            'delegacion',
            'codigo_postal',
            'manzana',
            'lote',
            'fracciones',
            'parcelas',
            'condominio',
            'unidad',
            'nombre_condominio',
            'valor_unitario_zona',
            'valor_unitario_predio',
            'valor_unitario_provicional',
            'superficie_construccion',
            'uso_suelo',
            'tasa',
            'frente_comun',
            'valor_fiscal',
            'fecha_alta',
            'fecha_vigencia',
            'clave_anterior',
            'comentario',
            'tipo',
            'minicipio',
            'estado',
            'pais',
            'sector',
            'tipo_persona',
        ]

        labels = {
            'nombre_propietario': 'Nombre del Propietario',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'representante_legal': 'Representante Legal',
            'numero_oficial': 'Número Oficial',
            'clave_catastral': 'Clave Catastral',
            'superficie': 'Superficie',
            'calle': 'Calle',
            'numero_exterior': 'Número Exterior',
            'numero_interior': 'Número Interior',
            'colonia': 'Colonia',
            'delegacion': 'Delegación',
            'codigo_postal': 'Código Postal',
            'manzana': 'Manzana',
            'lote': 'Lote',
            'fracciones': 'Fracciones',
            'parcelas': 'Parcelas',
            'condominio': 'Condominio',
            'unidad': 'Unidad',
            'nombre_condominio': 'Nombre del Condominio',
            'valor_unitario_zona': 'Valor Unitario Zona',
            'valor_unitario_predio': 'Valor Unitario Predio',
            'valor_unitario_provicional': 'Valor Unitario Provisional',
            'superficie_construccion': 'Superficie Construcción',
            'uso_suelo': 'Uso de Suelo',
            'tasa': 'Tasa',
            'frente_comun': 'Frente Común',
            'valor_fiscal': 'Valor Fiscal',
            'fecha_alta': 'Fecha de Alta',
            'fecha_vigencia': 'Fecha de Vigencia',
            'clave_anterior': 'Clave Anterior',
            'comentario': 'Comentario',
            'tipo': 'Tipo de Predio',
            'minicipio': 'Municipio',
            'estado': 'Estado',
            'pais': 'País',
            'sector': 'Sector',
            'tipo_persona': 'Tipo de Persona',
        }

        widgets = {
            'nombre_propietario': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'representante_legal': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_oficial': forms.TextInput(attrs={'class': 'form-control'}),
            'clave_catastral': forms.TextInput(attrs={'class': 'form-control'}),
            'superficie': forms.NumberInput(attrs={'class': 'form-control'}),
            'calle': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_exterior': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_interior': forms.TextInput(attrs={'class': 'form-control'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control'}),
            'delegacion': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'manzana': forms.TextInput(attrs={'class': 'form-control'}),
            'lote': forms.TextInput(attrs={'class': 'form-control'}),
            'fracciones': forms.TextInput(attrs={'class': 'form-control'}),
            'parcelas': forms.TextInput(attrs={'class': 'form-control'}),
            'condominio': forms.Select(attrs={'class': 'form-control'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_condominio': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_unitario_zona': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_unitario_predio': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_unitario_provicional': forms.NumberInput(attrs={'class': 'form-control'}),
            'superficie_construccion': forms.NumberInput(attrs={'class': 'form-control'}),
            'uso_suelo': forms.Select(attrs={'class': 'form-control'}),
            'tasa': forms.NumberInput(attrs={'class': 'form-control'}),
            'frente_comun': forms.Select(attrs={'class': 'form-control'}),
            'valor_fiscal': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_alta': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'fecha_vigencia': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'clave_anterior': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'sector': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_persona': forms.Select(attrs={'class': 'form-control'}),
        }


class NotificacionesForm(forms.ModelForm):
    nombre_propietario = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Notificaciones
        fields = ['datos','colindancias','rfc','curp','pensionado','nombre_casada','observaciones','opcion_tramite','numero_tramite']
        exclude = ['usuario_creacion', 'usuario_modificacion', 'estado']

        labels = {
            'datos': forms.Select(attrs={'class': 'form-control'}),
            'datos': 'Catastro',
            'colindancias': 'Colindancias',
            'rfc': 'RFC',
            'curp': 'CURP',
            'pensionado': 'Pensionado',
            'nombre_casada': 'Nombre Casada',
            'observaciones': 'Observaciones',
            'opcion_tramite': 'Opción de Trámite',
            'numero_tramite': 'Número de Trámite',
        }
        
        widgets = {
            'colindancias': forms.TextInput(attrs={'class': 'form-control'}),
            'rfc': forms.TextInput(attrs={'class': 'form-control'}),
            'curp': forms.TextInput(attrs={'class': 'form-control'}),
            'pensionado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nombre_casada': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'opcion_tramite': forms.Select(attrs={'class': 'form-control'}),
            'numero_tramite': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personalización de etiquetas
        self.fields['nombre_propietario'].label = 'Nombre del Propietario'
        self.fields['email'].label = 'Correo Electrónico'
        self.fields['telefono'].label = 'Teléfono'
        self.fields['direccion'].label = 'Dirección'

        # Si hay una instancia existente de Notificaciones, inicializar los datos de Catastro
        if self.instance.pk:
            catastro_instance = self.instance.datos
            self.fields['nombre_propietario'].initial = catastro_instance.nombre_propietario
            self.fields['email'].initial = catastro_instance.email
            self.fields['telefono'].initial = catastro_instance.telefono
            self.fields['direccion'].initial = catastro_instance.direccion

    def save(self, commit=True):
        notificaciones_instance = super().save(commit=commit)
        
        # Actualizar los datos de Catastro relacionados
        if commit:
            catastro_instance = notificaciones_instance.datos
            catastro_instance.nombre_propietario = self.cleaned_data['nombre_propietario']
            catastro_instance.email = self.cleaned_data['email']
            catastro_instance.telefono = self.cleaned_data['telefono']
            catastro_instance.direccion = self.cleaned_data['direccion']
            catastro_instance.save()

        return notificaciones_instance
