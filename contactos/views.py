import datetime
import time
import requests

from django.http 					import HttpResponse, Http404
from django.shortcuts 				import render_to_response, get_object_or_404

from django.template 				import RequestContext

from django.core.context_processors import csrf
from django.views.decorators.csrf 	import csrf_exempt, csrf_protect

from contactos.models 				import Contacto

from .forms							import ContactoForm
from .forms 						import ContactoForm2

#@csrf_exempt

def formulario(request):
	contactos = Contacto.objects.all()
	return render_to_response( 'contactos/index.html', {'contactos':contactos}, context_instance=RequestContext(request))

def index(request):

	if request.method == 'POST':

		form = ContactoForm2(request.POST)
		if form.is_valid():
			form.send_mail()
			return HttpResponse("Formulario esta ok.")

	else:

		form = ContactoForm2()

	return render_to_response('contactos/index.html', {'form': form}, context_instance=RequestContext(request))

#	

