from django 			import forms

from django.forms 		import ModelForm
from django.forms 		import Textarea

from django.db 			import models

from .models 			import Contacto

from django.core.mail 	import send_mail
from django.core.mail 	import EmailMultiAlternatives

TIPOS = ( 
	( 'sugerencia', 'Sugerencias' ),
	( 'error', 'Errores'),
	( 'contacto', 'Contacto'),
)

# el formulario por defecto

class ContactoForm(ModelForm):
    class Meta:
        model 	= Contacto
        fields 	= ('tipo', 'texto', 'mail')

# el formulario personalizado

class ContactoForm2(forms.Form):
	tipo	= forms.ChoiceField(choices=TIPOS)
	texto	= forms.CharField(widget=forms.Textarea(attrs={'cols': 180, 'rows': 10}))
	mail	= forms.EmailField(required=True)

	# el mesaje del comentario al menos debe contener 4 lineas

	def clean_texto(self):
		message = self.cleaned_data.get('texto', '')
		if len(message.split()) < 2:
			raise forms.ValidationError("Debe introducir al menos dos lineas.")
		return message

	def send_mail(self):
		mail = 	EmailMultiAlternatives( 'Feedback from your site, topic: %s' % self.cleaned_data.get('tipo'),
										self.cleaned_data.get('text'),
										self.cleaned_data.get('mail'),
										['mcalero@gestool.es'])
		mail.attach_alternative("<p>This is an <strong>important</strong> message.</p>", "text/html")
		mail.send()

class ContactoModel(models.Model):
	tipo	= forms.ChoiceField(choices=TIPOS)
	texto	= forms.CharField(widget=forms.Textarea(attrs={'cols': 180, 'rows': 10}))
	mail	= forms.EmailField(required=True)

	# el mesaje del comentario al menos debe contener 4 lineas

	def clean_texto(self):
		message = self.cleaned_data.get('texto', '')
		if len(message.split()) < 2:
			raise forms.ValidationError("Debe introducir al menos dos lineas.")
		return message

	def form_valid(self):
		send_mail('Feedback from your site, topic: %s' % tipo, texto, mail, ['mcalero@gestool.es'])
		return super(ContactoForm2, self).form_valid(form)

class ContactoFormModel(ModelForm):
	class Meta:
		model = ContactoModel

