from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.servicio.forms import SolicitudFormCreate, SolicitudFormUpdate
from apps.servicio.models import Servicio, Solicitud

def index(request):
	return render(request, 'servicio/index.html')

class ServicioList(ListView):
    model = Servicio    
    template_name = 'servicio/servicio_list.html'
    paginate_by = 2
    
#def SolicitudList(request):
#    solicitudes = Solicitud.objects.filter(usuario=request.user)
#    return render(request, 'servicio/solicitud_list.html', {'solicitudes': solicitudes})

class SolicitudList(ListView):     
    model = Solicitud        
 #   queryset=Solicitud.objects.filter(usuario=1)
    template_name = 'servicio/solicitud_list.html'
    paginate_by = 2
    
    def get_queryset(self):
        return self.model.objects.filter(usuario=self.request.user)

def SolicitudCreate(request):
    if request.method == 'POST':
        form = SolicitudFormCreate(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)  
            solicitud.usuario = request.user
            solicitud.save() 
            form.save()    
            return render(request,'servicio/guardado.html', {})
    else:
        form = SolicitudFormCreate()
    return render(request,'servicio/solicitud_Update.html', {'form': form})

#class SolicitudCreate(CreateView):
 #   model = Solicitud
  #  form_class = SolicitudFormCreate
 #   template_name = 'servicio/solicitud_update.html'
 #   success_url = reverse_lazy('servicio:solicitud_listar')

 #   def get_queryset(User):
 #       return User.objects.filter(id=User.request.user)

class SolicitudUpdate(UpdateView):
    model = Solicitud
    form_class = SolicitudFormUpdate
    template_name = 'servicio/solicitud_update.html'
    success_url = reverse_lazy('servicio:solicitud_listar')  
    
class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'servicio/solicitud_delete.html'
    success_url = reverse_lazy('servicio:solicitud_listar')
