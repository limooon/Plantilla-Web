from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Categorias,SubCategorias,Marca,UnidadMedida,Producto
from .forms import CategoriaForm,SubCategoriaForm,MarcaForm,UnidadMedidaForm,ProductoForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect,render

# vistas categorias
class CategoriaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Categorias
    template_name = 'inv/categorias.html'
    context_object_name = 'obj'
    login_url = 'core:login'
    permission_required = 'Inv.view_categoria'

class CreateViewCategorias(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Categorias
    template_name = "inv/categorias_form.html"
    form_class = CategoriaForm
    success_url = reverse_lazy("Inv:categoria_lista")
    login_url = 'core:login'
    permission_required = 'Inv.add_categoria'
    permission_denied_message = "No tienes permiso para agregar nuevas categorías."

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()

    def form_valid(self, form):
        # Verificar si ya existe una categoría con la misma descripción
        descripcion = form.cleaned_data['descripcion']
        if Categorias.objects.filter(descripcion=descripcion).exists():
            # Mostrar mensaje de error
            messages.error(self.request, 'Ya existe una categoría con esta descripción.')
            return self.form_invalid(form)

        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class CategoriaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Categorias
    template_name = "inv/categorias_form.html"
    form_class = CategoriaForm
    success_url = reverse_lazy('Inv:categoria_lista')
    login_url = 'core:login'
    permission_required = 'Inv.change_categoria'
    permission_denied_message = "No tienes permiso para modificar categorías."

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user
        return super().form_valid(form)
     
class CategoriaDeleteView(LoginRequiredMixin,DeleteView):
    model = Categorias
    template_name = "inv/categorias_delete.html"
    success_url = reverse_lazy('Inv:categoria_lista')
    login_url = 'core:login'
    
    
    
#vistas subcategoria
class SubCategoriasList(LoginRequiredMixin,ListView):
    model = SubCategorias
    context_object_name = 'obj'
    template_name='inv/subcategorias_list.html'
    login_url = 'core:login' 
    

class CreateViewSubCategorias(LoginRequiredMixin, CreateView):
    model = SubCategorias
    template_name = "inv/subcategorias_form.html"
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy("Inv:subcategorias-list")
    login_url = 'core:login'
    
    def form_valid(self, form):
        form.instance.usuario_creacion= self.request.user
        return super().form_valid(form)
    
    
class SubCategoriaUpdateView(LoginRequiredMixin,UpdateView):
    model = SubCategorias
    template_name = "inv/subcategorias_form.html"
    form_class = SubCategoriaForm
    success_url = reverse_lazy('Inv:subcategorias-list')
    login_url = 'core:login'
    
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)
    
class SubCategoriaDeleteView(LoginRequiredMixin,DeleteView):
    model = SubCategorias
    template_name = "inv/subcategorias_delete.html"
    success_url = reverse_lazy('Inv:subcategorias-list')
    login_url = 'core:login'
    
#vistas marca
class MarcaList(LoginRequiredMixin,ListView):
    model =  Marca
    context_object_name = 'obj'
    template_name='inv/marca_list.html'
    login_url = 'core:login' 
    
class  MarcaCreateView(LoginRequiredMixin, CreateView):
    model =  Marca
    template_name = "inv/marca_form.html"
    context_object_name = 'obj'
    form_class =  MarcaForm
    success_url = reverse_lazy("Inv:marca-list")
    login_url = 'core:login'
    
    def form_valid(self, form):
        form.instance.usuario_creacion= self.request.user
        return super().form_valid(form)
    
class MarcaUpdateView(LoginRequiredMixin,UpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    form_class =  MarcaForm
    success_url = reverse_lazy('Inv:marca-list')
    login_url = 'core:login'
    
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)
    
    
def marca_inactivar(request,pk):
    marca = Marca.objects.filter(pk=pk).first()
    contexto={}
    template = "inv/catalogo_inactivar.html"
    
    if not marca:
        return redirect("Inv:marca-list")
    
    if request.method == "GET":
        contexto ={'obj': marca}
        
    if request.method == "POST":
        marca.estado = False
        marca.save()
        return redirect("Inv:marca-list")
    
    return render(request,template,contexto)
    
#vistas de unidad de medida
class UnidadMedidaListView(LoginRequiredMixin, ListView):
    model = UnidadMedida
    context_object_name = 'obj'
    template_name = 'inv/medida_list.html'

class UnidadMedidaCreateView(LoginRequiredMixin, CreateView):
    model =  UnidadMedida
    template_name = "inv/medida_form.html"
    context_object_name = 'obj'
    form_class =  UnidadMedidaForm
    success_url = reverse_lazy("Inv:medida-list")
    login_url = 'core:login'
    
    def form_valid(self, form):
        form.instance.usuario_creacion= self.request.user
        return super().form_valid(form)

class UnidadMedidaUpdateView(LoginRequiredMixin,UpdateView):
    model = UnidadMedida
    template_name = "inv/medida_form.html"
    form_class =  UnidadMedidaForm
    success_url = reverse_lazy('Inv:medida-list')
    login_url = 'core:login'
    
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)
    
def um_inactivar(request,pk):
    um =UnidadMedida.objects.filter(pk=pk).first()
    contexto = {}
    template = "inv/um_inactivar.html"
    
    if not um:
        return redirect('Inv:medida-list')
   
    if request.method == "GET":
        contexto ={'obj': um}
        
    if request.method == "POST":
        um.estado = False
        um.save()
        return redirect("Inv:medida-list")
    
    return render(request,template,contexto)



#vistas modelo producto
class ProductoListView(LoginRequiredMixin, ListView):
    model =  Producto
    context_object_name = 'obj'
    template_name = 'inv/producto_list.html'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model =   Producto
    template_name = "inv/producto_form.html"
    context_object_name = 'obj'
    form_class =  ProductoForm
    success_url = reverse_lazy("Inv:producto-list")
    login_url = 'core:login'
    
    def form_valid(self, form):
        form.instance.usuario_creacion= self.request.user
        return super().form_valid(form)

class ProductoUpdateView(LoginRequiredMixin,UpdateView):
    model =  Producto
    template_name = "inv/producto_form.html"
    form_class =  ProductoForm
    success_url = reverse_lazy('Inv:producto-list')
    login_url = 'core:login'
    
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)
    
def  Producto_inactivar(request,pk):
    producto = Producto.objects.filter(pk=pk).first()
    contexto = {}
    template = "inv/um_inactivar.html"
    
    if not producto:
        return redirect('Inv:producto-list')
   
    if request.method == "GET":
        contexto ={'obj': producto}
        
    if request.method == "POST":
        producto.estado = False
        producto.save()
        return redirect("Inv:producto-list")
    
    return render(request,template,contexto)