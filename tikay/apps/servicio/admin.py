from django.contrib import admin
from apps.servicio.models import Area, Servicio, Solicitud, Informacion

class AreaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre')

class ServicioAdmin(admin.ModelAdmin):
	list_display = ('area', 'nombre')
	list_filter = ('area',)
	search_fields = ('nombre', 'area__nombre')
#	list_editable = ('nombre',)

class SolicitudAdmin(admin.ModelAdmin):
	list_display = ('fecha_solicitud', 'hora_solicitud', 'usuario')
	list_filter = ('usuario', 'fecha_solicitud')
	filter_horizontal = ('servicio',)	

class InformacionAdmin(admin.ModelAdmin):
	list_display = ('id','categoria_titulo', 'categoria_link',
	                'enlace_titulo', 'enlace_link',
	                'testigo_texto', 'testigo_autor', 'testigo_profission', 'testigo_link',
	                'ult_actualizacion_titulo', 'ult_actualizacion_texto', 'ult_actualizacion_link',
	                'video_titulo', 'video_sub_titulo', 'video_texto','video_link', 'video_imagen'
	                 )
#	list_filter = ('titulo_Actualizacion', 'texto_Actualizacion')
	
# Register your models here.
admin.site.register(Area, AreaAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Informacion, InformacionAdmin)