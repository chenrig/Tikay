from django.contrib import admin
from apps.servicio.models import Area, Servicio, Solicitud

class ServicioAdmin(admin.ModelAdmin):
	list_display = ('area', 'nombre')
	list_filter = ('area',)
	search_fields = ('nombre', 'area__nombre')
#	list_editable = ('nombre',)

class SolicitudAdmin(admin.ModelAdmin):
	list_display = ('fecha_solicitud', 'hora_solicitud', 'usuario')
	list_filter = ('usuario', 'fecha_solicitud')
	filter_horizontal = ('servicio',)	

# Register your models here.
admin.site.register(Area)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
