from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from apps.servicio.forms import SolicitudFormCreate, SolicitudFormCreateCurto, SolicitudFormUpdate
from apps.servicio.models import Area, Servicio, Solicitud, Informacion
from apps.usuario.models import Perfiles

#def index(request):
#	return render(request, 'index.html')
##    return render(request, 'servicio/index.html')

class Index(ListView):
    model = Informacion 
    template_name = 'index.html'
#    paginate_by = 5

#def sobre(request):
#    return render(request, 'about.html')

class Sobre(ListView):
    model = Informacion    
    template_name = 'about.html'
#    paginate_by = 5

def Cadastro(request):
    return render(request, 'cadastro.html')

def Cadastrar(request):
 #   nombre = request.POST.get('nombre')
 #   nombre = request.POST.get('nombre', '') 
  #  apellido = request.POST.get('apellido', '')    
 #   correo = request.POST.get('correo', '')
 #   telefono = request.POST.get('telefono', '')
 #   celular = request.POST.get('celular', '')
    usuario = request.POST.get('usuario', '')
    contrasena1 = request.POST.get('contrasena1', '')
    contrasena2 = request.POST.get('contrasena2', '')    
 
    if usuario and contrasena1 and contrasena2:
        try:
            if contrasena1 == contrasena2:
                user = User()
                user.first_name = request.POST.get('nombre', '') 
                user.last_name = request.POST.get('apellido')
                user.email = request.POST.get('correo')
                user.username = request.POST.get('usuario')          
                user.set_password(request.POST.get('contrasena1'))          
                user.save()
                perfil = Perfiles()
                perfil.usuario = user
                perfil.telefono = request.POST.get('telefono')
                perfil.celular = request.POST.get('celular')  
                perfil.save()
                user = authenticate(username=user.username, password=user.password)
                return render(request,'index.html', {})
            else:
                return HttpResponse('Contraseñas no conferen')
        except BadHeaderError:  # sandraroncerosdepaz@gmail.com
            return HttpResponse('Contenido de cadastro invalido')
      #  return HttpResponseRedirect('servicio:contacto')      
        return render(request,'cadastro.html', {})
    else:        
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Contenido de cadastro invalido')

def Login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
      
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return render(request,'index.html', {})
        else:
            return HttpResponse('conta desabilitada') 
    else:
        return HttpResponse('login inválido')

def Logout(request):
    auth_logout(request)    
    return render(request,'index.html', {})

def Contacto(request):
    return render(request, 'contact.html')

class ListServicio(ListView):
    model = Servicio    
    template_name = 'servicio.html'
    paginate_by = 5

def Psicologia(request, template_name='psicologia.html'):
    area_list = Area.objects.all()
    id_area = 0

    for area in area_list:
        if area.nombre == "Psicologia":
           id_area = area.id

    serv = Servicio.objects.filter(area=id_area)

    paginator = Paginator(serv, 5) # exibe 5 servicios por pagina
    page = request.GET.get('page')
    try:
        servicio = paginator.page(page)
    except PageNotAnInteger:
        # Si page no es un inteiro, entrega la primer pagina.
        servicio = paginator.page(1)
    except EmptyPage:
        # si pagina está fora de faixa (ej. 9999), entrega ultima pagina de resultados.
        servicio = paginator.page(paginator.num_pages)
  
    data = {}
    data['object_list'] = servicio
    return render(request, template_name, data)

#class psicologia(ListView):
#    model = Servicio    
#    template_name = 'psicologia.html'
#    paginate_by = 5
#        
#    def get_queryset(self): 
#        return Servicio.objects.filter(area=id_area)

def Comunicacion(request, template_name='comunicacion.html'):
    area_list = Area.objects.all()
    id_area = 0

    for area in area_list:
        if area.nombre == "Comunicaciones":            
           id_area = area.id          

    serv = Servicio.objects.filter(area=id_area)

    paginator = Paginator(serv, 5) # exibe 5 servicios por pagina
    page = request.GET.get('page')
    try:
        servicio = paginator.page(page)
    except PageNotAnInteger:
        # Si page no es un inteiro, entrega la primer pagina.
        servicio = paginator.page(1)
    except EmptyPage:
        # si pagina está fora de faixa (ej. 9999), entrega ultima pagina de resultados.
        servicio = paginator.page(paginator.num_pages)
  
    data = {}
    data['object_list'] = servicio
    return render(request, template_name, data)

#class comunicacion(ListView):
#    model = Servicio    
#    template_name = 'comunicacion.html'
#    paginate_by = 5
    
#    def get_queryset(self):           
#        return self.model.objects.filter(area=5)

def Asesoria(request, template_name='asesoria.html'):
    area_list = Area.objects.all()
    id_area = 0

    for area in area_list:
        if area.nombre == "Asesoria":            
           id_area = area.id           

    serv = Servicio.objects.filter(area=id_area)

    paginator = Paginator(serv, 5) # exibe 5 servicios por pagina
    page = request.GET.get('page')
    try:
        servicio = paginator.page(page)
    except PageNotAnInteger:
        # Si page no es un inteiro, entrega la primer pagina.
        servicio = paginator.page(1)
    except EmptyPage:
        # si pagina está fora de faixa (ej. 9999), entrega ultima pagina de resultados.
        servicio = paginator.page(paginator.num_pages)
  
    data = {}
    data['object_list'] = servicio
    return render(request, template_name, data)
    
#class asesoria(ListView):
#    model = Servicio    
#    template_name = 'asesoria.html'
#    paginate_by = 5
#
#    def get_queryset(self): 
#        return Servicio.objects.filter(area=6)

def Importacion(request, template_name='importacion.html'):
    area_list = Area.objects.all()
    id_area = 0

    for area in area_list:
        if area.nombre == "Importacion":            
           id_area = area.id           

    serv = Servicio.objects.filter(area=id_area)

    paginator = Paginator(serv, 5) # exibe 5 servicios por pagina
    page = request.GET.get('page')
    try:
        servicio = paginator.page(page)
    except PageNotAnInteger:
        # Si page no es un inteiro, entrega la primer pagina.
        servicio = paginator.page(1)
    except EmptyPage:
        # si pagina está fora de faixa (ej. 9999), entrega ultima pagina de resultados.
        servicio = paginator.page(paginator.num_pages)
  
    data = {}
    data['object_list'] = servicio
    return render(request, template_name, data)

#class importacion(ListView):
#    model = Servicio    
#    template_name = 'importacion.html'
#    paginate_by = 5
#
#    def get_queryset(self): 
#        return Servicio.objects.filter(area=7)

def Exportacion(request, template_name='exportacion.html'):
    area_list = Area.objects.all()
    id_area = 0

    for area in area_list:
        if area.nombre == "Exportacion":            
           id_area = area.id           

    serv = Servicio.objects.filter(area=id_area)

    paginator = Paginator(serv, 5) # exibe 5 servicios por pagina
    page = request.GET.get('page')
    try:
        servicio = paginator.page(page)
    except PageNotAnInteger:
        # Si page no es un inteiro, entrega la primer pagina.
        servicio = paginator.page(1)
    except EmptyPage:
        # si pagina está fora de faixa (ej. 9999), entrega ultima pagina de resultados.
        servicio = paginator.page(paginator.num_pages)
  
    data = {}
    data['object_list'] = servicio
    return render(request, template_name, data)

#class exportacion(ListView):
#    model = Servicio    
#    template_name = 'exportacion.html'
#    paginate_by = 5
#
#    def get_queryset(self): 
#        return Servicio.objects.filter(area=8)

def Capacitacion(request, template_name='capacitacion.html'):
    area_list = Area.objects.all()
    id_area = 0

    for area in area_list:
        if area.nombre == "Capacitacion":            
           id_area = area.id          

    serv = Servicio.objects.filter(area=id_area)

    paginator = Paginator(serv, 5) # exibe 5 servicios por pagina
    page = request.GET.get('page')
    try:
        servicio = paginator.page(page)
    except PageNotAnInteger:
        # Si page no es un inteiro, entrega la primer pagina.
        servicio = paginator.page(1)
    except EmptyPage:
        # si pagina está fora de faixa (ej. 9999), entrega ultima pagina de resultados.
        servicio = paginator.page(paginator.num_pages)
  
    data = {}
    data['object_list'] = servicio
    return render(request, template_name, data)

#class capacitacion(ListView):
#    model = Servicio    
#    template_name = 'capacitacion.html'
#    paginate_by = 5
#
#    def get_queryset(self): 
#        return Servicio.objects.filter(area=9)
    
#def SolicitudList(request):
#    solicitudes = Solicitud.objects.filter(usuario=request.user)
#    return render(request, 'servicio/solicitud_list.html', {'solicitudes': solicitudes})

class ListSolicitud(ListView):     
    model = Solicitud        
 #   queryset=Solicitud.objects.filter(usuario=1)
  #  template_name = 'servicio/solicitud_list.html'
    template_name = 'solicitud.html'
    paginate_by = 5
    
    def get_queryset(self):
        return self.model.objects.filter(usuario=self.request.user)

def Create(request):
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

def Crear(request):
    
  #  def get_queryset(self):           
  #      return self.model.objects.filter(area=5)

 #   servicio = Servicio.objects.filter(area=5)
    
    if request.method == 'POST':
        form = SolicitudFormCreateCurto(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)  
            solicitud.usuario = request.user
            solicitud.save() 
            form.save()    
            return render(request,'servicio/guardado.html', {})
    else:
        form = SolicitudFormCreateCurto()
    return render(request,'crear.html', {'form': form})

def Editar(request, id_solicitud):
    
  #  def get_queryset(self):           
  #      return self.model.objects.filter(area=5)

 #   servicio = Servicio.objects.filter(area=5)
    solicitud = Solicitud.objects.get(id=id_solicitud)

    if request.method == 'GET':
        form = SolicitudFormCreateCurto(instance=solicitud)
    else:
        form = SolicitudFormCreateCurto(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()               
        return redirect('solicitud')
    
    return render(request,'update.html', {'form': form})

class Update(UpdateView):
    model = Solicitud
    form_class = SolicitudFormUpdate
    template_name = 'solicitud_update.html'
    success_url = reverse_lazy('solicitud')  
    
class Delete(DeleteView):
    model = Solicitud
    template_name = 'delete.html'
    success_url = reverse_lazy('servicio:solicitud')

def Email(request):
 #   nombre = request.POST.get('nombre')
    subject = request.POST.get('subject', '') 
    message = request.POST.get('message', '')
    email = request.POST.get('email', '')
    message2 = 'Gracias por solicitar nuestros servicios. Contactaremos en breve.'

 #   subject = subject + ' de ' + nombre 

    if subject and message and email:
        try:
            send_mail(subject, message, email, ['chenrig@gmail.com'])
            send_mail(subject, message2, 'chenrig@gmail.com', [email])
        except BadHeaderError:  # sandraroncerosdepaz@gmail.com
            return HttpResponse('Contenido de correo invalido')
      #  return HttpResponseRedirect('servicio:contacto')
        return render(request,'index.html', {})
    else:        
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Contenido de correo invalido')