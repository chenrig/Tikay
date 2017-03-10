from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.servicio.views import Index, Sobre, Cadastro, Cadastrar, Login, Logout, \
                                Contacto, Email, ListServicio, Psicologia, Comunicacion, \
                                Asesoria, Importacion, Exportacion, Capacitacion, Crear, Editar, \
                                ListSolicitud, Create, Update, Delete

urlpatterns = [
  #  url(r'^$', index, name='index'),
    url(r'^$', Index.as_view(), name='index'),
  #  url(r'^sobre', sobre, name='sobre'),
    url(r'^sobre', Sobre.as_view(), name='sobre'),
    url(r'^cadastro', Cadastro, name='cadastro'),
    url(r'^cadastrar', Cadastrar, name='cadastrar'),
    url(r'^login', Login, name='login'),        
    url(r'^logout', Logout, name='logout'),
    url(r'^contacto', Contacto, name='contacto'),
    url(r'^email', Email, name='email'),
    url(r'^servicio', ListServicio.as_view(), name='servicio'), 
   # url(r'^psicologia', psicologia.as_view(), name='psicologia'),
    url(r'^psicologia', Psicologia, name='psicologia'),
   # url(r'^comunicacion', comunicacion.as_view(), name='comunicacion'),  
    url(r'^comunicacion', Comunicacion, name='comunicacion'),  
  #  url(r'^asesoria', asesoria.as_view(), name='asesoria'),
    url(r'^asesoria', Asesoria, name='asesoria'),
   # url(r'^importacion', importacion.as_view(), name='importacion'),
    url(r'^importacion', Importacion, name='importacion'),
   # url(r'^exportacion', exportacion.as_view(), name='exportacion'),
    url(r'^exportacion', Exportacion, name='exportacion'),
  #  url(r'^capacitacion', capacitacion.as_view(), name='capacitacion'),
    url(r'^capacitacion', Capacitacion, name='capacitacion'),
    url(r'^nuevo$', login_required(Create), name='crear'), 
    url(r'^Crear', login_required(Crear), name='Crear'), 
 #   url(r'^Crear', login_required(Crear.as_view), name='Crear'),
 #   url(r'^nuevo$', login_required(SolicitudCreate.as_view()), name='solicitud_crear'), 
 #   url(r'^listar', login_required(SolicitudList), name='solicitud_listar'),  
   # url(r'^listar', login_required(SolicitudList.as_view()), name='solicitud_listar'),   
    url(r'^solicitud', login_required(ListSolicitud.as_view()), name='solicitud'),   
    url(r'^editar/(?P<id_solicitud>\d+)/$', login_required(Editar), name='editar'),   
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(Delete.as_view()), name='eliminar'),
]