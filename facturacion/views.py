from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm


#provedor  vistas
class ClienteList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Cliente
    context_object_name = 'obj'
    template_name='fac/cliente_list.html'
    login_url = "core/login"
    permission_required = 'cmp.view_cliente'
    

class ClienteCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Cliente
    template_name = "facturacion/clientes_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy('fac:clientes-lista')
    login_url = "core/login"
    permission_required = 'cmp.add_cliente'
    
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)
    
class ClienteUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Cliente
    template_name = "facturacion/clientes_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy('fac:clientes-lista')
    login_url = "core/login"
    permission_required = 'cmp.change_cliente'
    
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)
    
def cliente_inactivar(request, pk):
    cliente = Cliente.objects.filter(pk=pk).first()

    if not cliente:
        return redirect('fac:clientes-lista')

    if request.method == "GET":
        contexto = {'obj': cliente}
        return render(request, "facturacion/cliente_inactivar.html", contexto)

    if request.method == "POST":
        cliente.estado = False
        cliente.save()
        return redirect('fac:clientes-lista')
    
'''
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
    
'''