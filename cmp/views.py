from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ProvedorForm,ComprasForm,ComprasDetalleForm
from .models import Provedor,ComprasEncabezado,ComprasDetalle
from Inv.models import Producto
import datetime

#provedor  vistas
class ProvedorList(LoginRequiredMixin,ListView):
    model = Provedor
    context_object_name = 'obj'
    template_name='cmp/provedor_list.html'
    login_url = "core/login"

class ProvedorCreateView(LoginRequiredMixin,CreateView):
    model = Provedor
    template_name = "cmp/provedor_form.html"
    context_object_name = 'obj'
    form_class = ProvedorForm
    success_url = reverse_lazy('cmp:provedor_list')
    login_url = "core/login"
    
    def form_valid(self, form):
        form.instance.usuario_creacion_id = self.request.user.id  
        return super().form_valid(form)
    
class ProvedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Provedor
    template_name = "cmp/provedor_form.html"
    context_object_name = 'obj'
    form_class = ProvedorForm
    success_url = reverse_lazy('cmp:provedor_list')  
    login_url = "core/login"

def provedor_inactivar(request, pk):
    provedor = Provedor.objects.filter(pk=pk).first()

    if not provedor:
        return redirect('cmp:provedor_list')

    if request.method == "GET":
        contexto = {'obj': provedor}
        return render(request, "cmp/provedor_inactivar.html", contexto)

    if request.method == "POST":
        provedor.estado = False
        provedor.save()
        return redirect('cmp:provedor_list')


#vists de encabezado de compras
class ComprasView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = ComprasEncabezado
    context_object_name = 'obj'
    template_name='cmp/compras_list.html'
    permission_required = 'cmp.view_comprasencabezado'
     
class CreateViewCompras(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ComprasEncabezado
    template_name = "cmp/compras_form.html"
    form_class = ComprasForm
    success_url = reverse_lazy("cmp:compras_list")
    login_url = 'core:login'
    permission_required = 'cmp.add_comprasencabezado'
    permission_denied_message = "No tienes permiso para agregar nuevas compras."

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class ComprasUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ComprasEncabezado
    template_name = "cmp/compras_form.html"
    form_class = ComprasForm
    success_url = reverse_lazy("cmp:compras_list")
    login_url = 'core:login'
    permission_required = 'cmp.change_comprasencabezado'
    permission_denied_message = "No tienes permiso para modificar cla compra."

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user
        return super().form_valid(form)
     
class ComprasDeleteView(LoginRequiredMixin,DeleteView):
    model = ComprasEncabezado
    template_name = "cmp/compras_delete.html"
    success_url = reverse_lazy('cmp:compras_list')
    login_url = 'core:login'



#vistas de compras detalle e imprecion
class ComprasDetalleListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ComprasDetalle
    context_object_name = 'detalles'
    template_name = 'cmp/compras.html'
    permission_required = 'cmp.view_comprasdetalle'

    
class ComprasDetalleCreateView(LoginRequiredMixin,CreateView):
    model = ComprasDetalle
    form_class = ComprasDetalleForm
    template_name = 'cmp/comprasDetalles_form.html'
    success_url = reverse_lazy('cmp:compras_detalle')

    def form_valid(self, form):
        return super().form_valid(form)

class ComprasDetalleUpdateView(UpdateView):
    model = ComprasDetalle
    form_class = ComprasDetalleForm
    template_name = 'cmp/comprasDetalles_form.html'
    success_url = reverse_lazy('cmp:compras_detalle')

    def form_valid(self, form):
        return super().form_valid(form)
    
class ComprasDetalleDeleteView(LoginRequiredMixin,DeleteView):
    model = ComprasDetalle
    template_name = "cmp/compras_delete.html"
    success_url = reverse_lazy('cmp:compras_detalle')
    login_url = 'core:login'

#vistas de compras detalle

'''class ProductoDetalleListView(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'cmp/compras.html'

    def get_queryset(self):
        return Producto.objects.filter(estado=True)  # Filtrar los productos activos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
'''
def Producto_inactivar(request,pk):
    pr = Producto.objects.filter(pk=pk).first()
    contexto={}
    template = "cmp/producto_inactivar.html"
    
    if not pr:
        return redirect("cmp:compras_list")
    
    if request.method == "GET":
        contexto ={'obj': pr}
        
    if request.method == "POST":
        pr.estado = False
        pr.save()
        return redirect("cmp:compras_list")
    
    return render(request,template,contexto)

'''
class ProductoDetalleListView(ListView):
    model = ComprasDetalle  # Modelo principal para la vista
    context_object_name = 'detalles'  # Nombre del contexto para los detalles de compra
    template_name = 'cmp/compras.html'  # Plantilla donde se mostrarán los detalles y los productos

    def get_queryset(self):
        # Filtrar los detalles de compra según sea necesario
        queryset = super().get_queryset()
        queryset = queryset.select_related('producto')  # Acceder a la descripción del producto
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar productos activos al contexto
        context['productos'] = Producto.objects.filter(estado=True)
        return context

'''

def detalles_y_productos(request):
    # Obtener los detalles de compra
    detalles = ComprasDetalle.objects.all() 

    # Obtener los productos activos
    productos = Producto.objects.filter(estado=True)

    # Renderizar la plantilla con ambos contextos
    return render(request, 'cmp/compras.html', {'detalles': detalles, 'productos': productos})


def productoslist(request):
    productos = Producto.objects.filter(estado=True)
    
    return render(request, 'cmp/productos.html', {'productos': productos})


    #toma datos d edos modelos y los integra en un solo objeto
def get_compras(request, compra_id=None):
    template = "cmp/compras.html"
    productos = Producto.objects.filter(estado=True)
    form_compras = ComprasForm()
    encabezado = None
    detalles = []

    if compra_id:
        encabezado = ComprasEncabezado.objects.filter(pk=compra_id).first()
        if encabezado:
            detalles = ComprasDetalle.objects.filter(compra=encabezado)
            fecha_compras = encabezado.fecha_compras.isoformat() if encabezado.fecha_compras else ''
            fecha_factura = encabezado.fecha_factura.isoformat() if encabezado.fecha_factura else ''
            
            e = {
                'fecha_compras': fecha_compras,
                'fecha_factura': fecha_factura,
                'observacion': encabezado.observacion,
                'proveedor': encabezado.proveedor,
                'no_factura': encabezado.no_factura,
                'sub_total': encabezado.sub_total,
                'descuento': encabezado.descuento,
                'total': encabezado.total
            }
            
            form_compras = ComprasForm(initial=e)
    
    contexto = {
        'productos': productos,
        'encabezado': encabezado,
        'detalles': detalles,
        'form_enc': form_compras
    }
    
    return render(request, template, contexto)