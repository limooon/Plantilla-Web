from django import forms
from .models import Provedor,ComprasEncabezado,ComprasDetalle

class ProvedorForm(forms.ModelForm):
    class Meta:
        model = Provedor
        fields = ('descripcion', 'direcion', 'contacto', 'telefono', 'email','estado')

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'direcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contacto'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input ml-2'}),
        }

class ComprasForm(forms.ModelForm):
    class Meta:
        model = ComprasEncabezado
        fields = ('fecha_compra', 'observacion', 'no_factura', 'fecha_factura', 'sub_total', 'descuento', 'total', 'provedor')

        widgets = {
            'fecha_compra': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de compra', 'type': 'date', 'readonly': 'true'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observación', 'rows': 3}),
            'no_factura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de factura'}),
            'fecha_factura': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de factura', 'type': 'date', 'readonly': 'true'}),
            'sub_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Subtotal', 'readonly': 'true'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Descuento', 'readonly': 'true'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total', 'readonly': 'true'}),
            'provedor': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        sub_total = cleaned_data.get('sub_total')
        descuento = cleaned_data.get('descuento')

        if sub_total is not None and descuento is not None:
            if descuento > sub_total:
                raise forms.ValidationError('El descuento no puede ser mayor al subtotal.')

        return cleaned_data
    
    
class ComprasDetalleForm(forms.ModelForm):
    class Meta:
        model = ComprasDetalle
        fields = ('producto', 'cantidad', 'precio_prv', 'descuento', 'costo')

        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
            'precio_prv': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Descuento'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Costo'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        precio_prv = cleaned_data.get('precio_prv')
        descuento = cleaned_data.get('descuento')

        if cantidad is not None and precio_prv is not None:
            sub_total = cantidad * precio_prv
            cleaned_data['sub_total'] = sub_total

        if sub_total is not None and descuento is not None:
            total = sub_total - descuento
            cleaned_data['total'] = total

        return cleaned_data