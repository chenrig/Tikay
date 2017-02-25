from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.core.signals import request_finished

class Area(models.Model):
	nombre = models.CharField(max_length=100)

	class Meta:
		ordering = ['nombre'] 

	def __str__(self):
		return '{}'.format(self.nombre)

class Servicio(models.Model):
	nombre = models.CharField(max_length=400)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)

	class Meta:
		ordering = ['area', 'nombre'] 

	def __str__(self):
		return '{}'.format(self.nombre)
		
class Solicitud(models.Model):		
	fecha_solicitud = models.DateField()
	hora_solicitud = models.TimeField()
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	servicio = models.ManyToManyField(Servicio)

	class Meta:
		ordering = ['fecha_solicitud', 'hora_solicitud'] 

	def __str__(self):
		return self.usuario.username	

def envia_email(**kwargs):
	try:
	    solic = kwargs['instance']
	except KeyError:
		return

	send_mail(
        'Servicio solicitado por: ' + str(solic.usuario),
        'En: ' + str(solic.fecha_solicitud.strftime('%d/%m/%Y')) + ' as ' + str(solic.hora_solicitud),
        'chenrig@gmail.com',
        ['chenrig@gmail.com', 'sandraroncerosdepaz@gmail.com'],
        )

models.signals.post_save.connect(envia_email, sender=Solicitud,
    dispatch_uid="servicio.models.Solicitud")

request_finished.connect(envia_email, dispatch_uid="servicio.models.Solicitud")	