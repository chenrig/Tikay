from django import forms

from apps.servicio.models import Solicitud

class SolicitudFormCreate(forms.ModelForm):

	class Meta:
		model = Solicitud

		fields = [            
            'fecha_solicitud',
            'hora_solicitud',
        #    'usuario',
            'servicio',
		]
		labels = {
		'fecha_solicitud': 'Fecha de Solicitud',
            'hora_solicitud': 'Hora de Solicitud',            
         #   'usuario': 'Usuario',
            'servicio': 'Servicio',
		}
		widgets = {		
            'fecha_solicitud': forms.TextInput(attrs={'class':'form-control'}),
            'hora_solicitud': forms.TextInput(attrs={'class':'form-control'}),
          #  'usuario': forms.Select(attrs={'class':'form-control'}),
          #  'usuario': forms.TextInput(attrs={'class':'form-control'}),
            'servicio': forms.CheckboxSelectMultiple(),
        }

class SolicitudFormCreateCurto(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [            
        #    'fecha_solicitud',
        #    'hora_solicitud',
        #    'usuario',
            'servicio',
        ]
        labels = {
         # 'fecha_solicitud': 'Fecha de Solicitud',
         #   'hora_solicitud': 'Hora de Solicitud',            
         #   'usuario': 'Usuario',
            'servicio': 'Servicios',
        }
        widgets = {     
          #  'fecha_solicitud': forms.TextInput(attrs={'class':'form-control'}),
          #  'hora_solicitud': forms.TextInput(attrs={'class':'form-control'}),
          #  'usuario': forms.Select(attrs={'class':'form-control'}),
          #  'usuario': forms.TextInput(attrs={'class':'form-control'}),
            'servicio': forms.CheckboxSelectMultiple(),
        }

class SolicitudFormUpdate(forms.ModelForm):

      class Meta:
            model = Solicitud

            fields = [            
            'fecha_solicitud',
            'hora_solicitud',            
            'servicio',
            ]
            labels = {
            'fecha_solicitud': 'Fecha de Solicitud',
            'hora_solicitud': 'Hora de Solicitud',             
            'servicio': 'Servicio',
            }
            widgets = {       
            'fecha_solicitud': forms.TextInput(attrs={'class':'form-control'}),
            'hora_solicitud': forms.TextInput(attrs={'class':'form-control'}),            
            'servicio': forms.CheckboxSelectMultiple(),
        }