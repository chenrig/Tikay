from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.core.signals import request_finished
from django.utils import timezone

class Area(models.Model):
	nombre = models.CharField(max_length=100)

	class Meta:
		ordering = ['nombre']

#	def __str__(self):
#		return "%s (ID:%s)" % (self.nombre, self.id)	
	
	def __str__(self):
		return '{}'.format(self.nombre)	

class Servicio(models.Model):
	nombre = models.CharField(max_length=400)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)

	class Meta:
		ordering = ['area', 'nombre'] 

	def __str__(self):
		return '{}'.format(self.nombre)

#	def __str__(self):
#		return self.area.nombre	

class Solicitud(models.Model):		
	fecha_solicitud = models.DateField(default=timezone.now)
	hora_solicitud = models.TimeField(default=timezone.now)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	servicio = models.ManyToManyField(Servicio)

	class Meta:
		ordering = ['usuario', 'fecha_solicitud', 'hora_solicitud'] 

	def __str__(self):
		return self.usuario.username

	def __str__(self):
		return '{}'.format(self.servicio)

	def publish(self):
		self.fecha_solicitud = timezone.now()
		self.save()

class Informacion(models.Model):
	categoria_titulo = models.CharField(max_length=100, null=True, blank= True, default=' ')
	categoria_link = models.CharField(max_length=100, null=True, blank= True, default='#')	
	enlace_titulo = models.CharField(max_length=100, null=True, blank= True, default=' ')
	enlace_link = models.CharField(max_length=100, null=True, blank= True, default='#')    	
	testigo_texto = models.CharField(max_length=400, null=True, blank= True, default=' ')
	testigo_autor = models.CharField(max_length=100, null=True, blank= True, default=' ')
	testigo_profission = models.CharField(max_length=100, null=True, blank= True, default=' ')	
	testigo_link = models.CharField(max_length=100, null=True, blank= True, default='#')    	
	ult_actualizacion_titulo = models.CharField(max_length=100, null=True, blank= True, default=' ')
	ult_actualizacion_texto = models.CharField(max_length=400, null=True, blank= True, default=' ')
	ult_actualizacion_link = models.CharField(max_length=100, null=True, blank= True, default='#')
	video_titulo = models.CharField(max_length=100, null=True, blank= True, default=' ')
	video_sub_titulo = models.CharField(max_length=100, null=True, blank= True, default=' ')
	video_texto = models.CharField(max_length=400, null=True, blank= True, default=' ')
	video_link = models.CharField(max_length=100, null=True, blank= True, default='#')
	video_imagen = models.ImageField(upload_to='galeria', null=True, blank= True)	

	class Meta:
		ordering = ['id',] 

def envia_email(**kwargs):
	try:
	    solic = kwargs['instance']
	except KeyError:
		return

	send_mail(
        'Servicio solicitado por: ' + str(solic.usuario),
        'En: ' + str(solic.fecha_solicitud.strftime('%d/%m/%Y')) + ' as ' + str(solic.hora_solicitud),
        'chenrig@gmail.com',
        ['chenrig@gmail.com',], fail_silently=False,
        ) # 'sandraroncerosdepaz@gmail.com'
	print (User.email)
#	send_mail(
 #       'Servicio solicitado por: ' + str(solic.usuario),
 #       'En: ' + str(solic.fecha_solicitud.strftime('%d/%m/%Y')) + ' as ' + str(solic.hora_solicitud) + 'Gracias por solicitar nuestros servicios. Contactaremos en breve.',
 #       'chenrig@gmail.com',
 #       [User.email,], fail_silently=False,
 #       ) # 'sandraroncerosdepaz@gmail.com'

models.signals.post_save.connect(envia_email, sender=Solicitud,
    dispatch_uid="servicio.models.Solicitud")

request_finished.connect(envia_email, dispatch_uid="servicio.models.Solicitud")	