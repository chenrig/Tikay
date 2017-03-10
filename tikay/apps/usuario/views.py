from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm
from .models import Perfiles

class Registrar(FormView):
#	template_name = 'cadastro.html'
	template_name = 'cadastro.html'
	form_class = UserForm
#	success_url = reverse_lazy('registrar')
	success_url = reverse_lazy('index')

	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario = user
		perfil.telefono = form.cleaned_data['telefono']
		perfil.celular = form.cleaned_data['celular']	
		perfil.save()
		return super(Registrar , self).form_valid(form)
