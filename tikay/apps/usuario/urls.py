from django.conf.urls import url
from apps.usuario.views import Registrar

urlpatterns = [
    url(r'^registrar', Registrar.as_view(), name="registrar"),    
]