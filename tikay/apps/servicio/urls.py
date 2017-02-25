from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.servicio.views import index, ServicioList, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^servicio', ServicioList.as_view(), name='servicio_listar'), 
    url(r'^nuevo$', login_required(SolicitudCreate), name='solicitud_crear'), 
 #   url(r'^nuevo$', login_required(SolicitudCreate.as_view()), name='solicitud_crear'), 
 #   url(r'^listar', login_required(SolicitudList), name='solicitud_listar'),  
    url(r'^listar', login_required(SolicitudList.as_view()), name='solicitud_listar'),   
    url(r'^editar/(?P<pk>\d+)/$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),   
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]