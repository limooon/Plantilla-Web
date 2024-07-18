from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView,TemplateView
from django.urls import reverse_lazy
from .models import Catastro,Notificaciones
from .forms import CatastroForm,NotificacionesForm




#provedor  vistas
class CatastroList(LoginRequiredMixin,ListView):
    model = Catastro
    context_object_name = 'obj'
    template_name = "Control-Urbano/ControlUrbano_list.html"
    login_url = "core/login"
    

class CatastroCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Catastro
    template_name = "Control-Urbano/ControlUrbano_form.html"
    form_class = CatastroForm
    success_url = reverse_lazy('ControlUrbano:registros_lista')
    login_url = "core/login"
    permission_required = 'ControlUrbano.add_catastro'
    
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)
    
class CatastroUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Catastro
    template_name = "Control-Urbano/ControlUrbano_form.html"
    form_class = CatastroForm
    success_url = reverse_lazy('ControlUrbano:registros_lista')
    login_url = "core/login"
    permission_required = 'ControlUrbano.change_catastro'
    
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class CatastroDeleteView(LoginRequiredMixin,DeleteView):
    model = Catastro
    template_name = "Control-Urbano/ControlUrbano_delete.html"
    success_url = reverse_lazy('ControlUrbano:registros_lista')
    login_url = 'core:login'
    permission_required = 'ControlUrbano.delete_catastro'

class CatastroDetailView(LoginRequiredMixin, DetailView):
    model = Catastro
    template_name = 'Control-Urbano/ControlUrbano_detalle.html'
    login_url = 'core:login'
    context_object_name = 'catastro'


#vistas de notificaciones
class Notificaion(LoginRequiredMixin,TemplateView):
    template_name = "Control-Urbano/notificaciones/noti.html"
    login_url = '/login'

class NotificacionesList(LoginRequiredMixin, ListView):
    model = Notificaciones
    context_object_name = 'obj'
    template_name = "Control-Urbano/notificaciones/notificacion_list.html"
    login_url = "core:login"

class NotificacionesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Notificaciones
    template_name = "Control-Urbano/notificaciones/notificacion_form.html"
    form_class = NotificacionesForm
    success_url = reverse_lazy('ControlUrbano:notificaciones_lista')
    login_url = "core:login"
    permission_required = 'ControlUrbano.add_notificaciones'

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)
 
class NotificacionesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Notificaciones
    template_name = "Control-Urbano/notificaciones/notificacion_form.html"
    form_class = NotificacionesForm
    success_url = reverse_lazy('ControlUrbano:notificaciones_lista')
    login_url = "core:login"
    permission_required = 'ControlUrbano.change_notificaciones'

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class NotificacionesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Notificaciones
    template_name = "Control-Urbano/notificaciones/notificacion_delete.html"
    success_url = reverse_lazy('ControlUrbano:notificaciones_lista')
    login_url = 'core:login'
    permission_required = 'ControlUrbano.delete_notificaciones'
    
class NotificacionesDetailView(LoginRequiredMixin, DetailView):
    model = Notificaciones
    template_name = 'Control-Urbano/notificaciones/notificacion_detalle.html'
    login_url = 'core:login'
    context_object_name = 'obj'


