
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("nombres", "apellidos", "celular", "tipo","estado")
        labels = {
            "nombres": "Nombres",
            "apellidos": "Apellidos",
            "celular": "Celular",
            "tipo": "Tipo de Cliente",
            "estado": "Estado",
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input ml-2'}),
        }
