from django import forms
from .models import Categorias,SubCategorias,Marca,UnidadMedida,Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ("descripcion", "estado")
        labels = {"descripcion": "Descripción de la categoría", "estado": "Estado"}
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input ml-2'}),
        }

class SubCategoriaForm(forms.ModelForm):
    #solo aparescan las categorias activas
    categoria = forms.ModelChoiceField(
        queryset = Categorias.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model = SubCategorias
        fields = ("categoria", "descripcion","estado")
        labels = {"descripcion": "Descripción de la categoría", "estado": "Estado"}
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ("descripcion", "estado")
        labels = {"descripcion": "Descripción de la marca", "estado": "Estado"}
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input ml-2'}),
        }
        
class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ("descripcion", "estado")
        labels = {"descripcion": "Descripción de la marca", "estado": "Estado"}
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input ml-2'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("codigo", "codigo_barra", "descripcion", "precio", "existencia", "ultima_compra", "marca", "unidad_medida", "subcategoria","estado")
        labels = {
            "codigo": "Código",
            "codigo_barra": "Código de Barras",
            "descripcion": "Descripción",
            "precio": "Precio",
            "existencia": "Existencia",
            "ultima_compra": "Última Compra",
            "marca": "Marca",
            "unidad_medida": "Unidad de Medida",
            "subcategoria": "Subcategoría",
            "estado": "Estado",
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_barra': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'existencia': forms.NumberInput(attrs={'class': 'form-control','readonly': 'true'}),
            'ultima_compra': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': 'true'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-control'}),
            'subcategoria': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input ml-2'}),
        }