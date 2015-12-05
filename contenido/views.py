# -*- coding: utf-8 -*-
import json
import glob

def imagenes_json(request):
	response = []
	jpg=glob.glob('media/uploads/*.jpg')
	png=glob.glob('media/uploads/*.png')
	for i in jpg:
		response.append({ "thumb": i, "image": i, "title": i })
	for i in png:
		response.append({ "thumb": i, "image": i, "title": i })
	return HttpResponse(json.dumps(response), content_type = "application/json")

from django.shortcuts import render_to_response
from django.template import RequestContext
from contenido.forms import ContenidoForm
from django.http import HttpResponse
from contenido.models import *
from django.http import HttpResponseRedirect
from contenido.forms import *
from django.template import Context
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import permission_required
from django.conf import settings
from django.template import Context
from django.template.loader import get_template

def inicio(request):
	documentos=Documento.objects.filter(tipo="D").order_by('-id')
	licitaciones=Documento.objects.filter(tipo="L").order_by('-id')
	return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def dondeEstamos(request):
	return render_to_response('dondeEstamos.html', locals(), context_instance=RequestContext(request))

def servicios(request):
	return render_to_response('servicios.html', locals(), context_instance=RequestContext(request))

@permission_required('contenido.add_contenido', login_url='/ingresar')
def crear_contenido(request):
	if request.method=='POST':
		form = ContenidoForm(request.POST or None, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/crear_contenido')
	else:
		form = ContenidoForm()
	return render_to_response('contenido.html', locals(), context_instance=RequestContext(request))

@permission_required('contenido.add_documento', login_url='/ingresar')
def subir_documento(request):
	documentos=Documento.objects.filter(tipo="D").order_by('-id')
	if request.method=='POST':
		form = DocumentoForm(request.POST, request.FILES)
		if form.is_valid():
			obj=form.save()
			obj.usuario=request.user
			obj.tipo="D"
			obj.save()
			return HttpResponseRedirect('/subirDocumento')
	else:
		form = DocumentoForm()
	return render_to_response('subirDocumento.html', locals(), context_instance=RequestContext(request))

@permission_required('contenido.change_documento', login_url='/ingresar')
def editar_documento(request, id):
	documento=Documento.objects.get(id=id)
	if request.method=='POST':
		form = DocumentoForm(request.POST, request.FILES, instance=documento)
		if form.is_valid():
			obj=form.save()
			obj.usuario=request.user
			obj.tipo="D"
			obj.save()
			return HttpResponseRedirect('/verDocumentos')
	else:
		form = DocumentoForm(instance=documento)
	return render_to_response('subirDocumento.html', locals(), context_instance=RequestContext(request))

@permission_required('contenido.delete_documento', login_url='/ingresar')
def eliminar_documento(request, id):
	modelo="Documento"
	objeto=Documento.objects.get(id=id)
	return render_to_response('eliminarDocumento.html', locals(), context_instance=RequestContext(request))

@permission_required('contenido.delete_documento', login_url='/ingresar')
def confirmar_eliminar_documento(request, id):
	documento=Documento.objects.get(id=id)
	documento.delete()
	return HttpResponseRedirect('/verDocumentos')

@permission_required('contenido.add_licitacion', login_url='/ingresar')
def subir_licitacion(request):
	documentos=Documento.objects.filter(tipo="L").order_by('-id')
	if request.method=='POST':
		form = DocumentoForm(request.POST, request.FILES)
		if form.is_valid():
			obj=form.save()
			obj.usuario=request.user
			obj.tipo="L"
			obj.save()
			return HttpResponseRedirect('/subirLicitacion')
	else:
		form = DocumentoForm()
	return render_to_response('subirLicitacion.html', locals(), context_instance=RequestContext(request))

@permission_required('contenido.change_mision', login_url='/ingresar')
def editar_conocenos(request):
	mision=Mision.objects.get()
	vision=Vision.objects.get()
	historia=Historia.objects.get()
	if request.method=='POST':
		form1 = MisionForm(request.POST, request.FILES, prefix="mis")
		form2 = VisionForm(request.POST, request.FILES, prefix="vis")
		form3 = HistoriaForm(request.POST, request.FILES, prefix="his")
		if form1.is_valid() and form2.is_valid() and form3.is_valid():
			form1.save()
			form2.save()
			form3.save()
			return HttpResponseRedirect('/editarConocenos')
	else:
		form1 = MisionForm(instance=mision, prefix="mis")
		form2 = VisionForm(instance=vision, prefix="vis")
		form3 = HistoriaForm(instance=historia, prefix="his")
	return render_to_response('conocenos.html', locals(), context_instance=RequestContext(request))

def conocenos(request):
	mision=Mision.objects.get()
	vision=Vision.objects.get()
	historia=Historia.objects.get()
	return render_to_response('conocenos.html', locals(), context_instance=RequestContext(request))

def contactenos(request):
	if request.method=='POST':
		subject = request.POST.get('asunto', '')
		message = request.POST.get('mensage', '')
		from_email = request.POST.get('email', '')
		name = request.POST.get('nombre', '')
		if subject and message and from_email and name:
			try:
				send_mail(
					subject,
					get_template('email.html').render(
						Context({
							'subject': request.POST.get('asunto', ''),
							'message' :request.POST.get('mensage', ''),
							'from_email': request.POST.get('email', ''),
							'name' :request.POST.get('nombre', ''),
							})
						),
					settings.EMAIL_HOST_USER,
					['jorge.lozano@uptc.edu.co'],
					fail_silently = False
				)
			except BadHeaderError:
				return HttpResponse('Cabecera invalida encontrada.')
			return HttpResponseRedirect('/gracias')
	else:
		return render_to_response('contactenos.html', {'form': ContactForm()}, context_instance=RequestContext(request))

def gracias_contacto(request):
		return render_to_response('gracias.html')

def ver_contenido(request):
	contenido=Pagina.objects.all()
	return render_to_response('verContenido.html', locals(), context_instance=RequestContext(request))

def pqr(request):
	pqr=PQR.objects.all()
	return render_to_response('PQR.html', locals(), context_instance=RequestContext(request))

def legalidad(request):
	return render_to_response('Legalidad.html', locals(), context_instance=RequestContext(request))

def verDocumentos(request):
	titulo="Últimas Novedades"
	documentos=Documento.objects.filter(tipo="D").order_by('-id')
	return render_to_response('verDocumentos.html', locals(), context_instance=RequestContext(request))

def verLicitaciones(request):
	titulo="Últimas Licitaciones"
	documentos=Documento.objects.filter(tipo="L").order_by('-id')
	return render_to_response('verDocumentos.html', locals(), context_instance=RequestContext(request))

@permission_required('contenido.add_pqr', login_url='/ingresar')
def crear_pqr(request):
	pqr=PQR.objects.all()
	if request.method=='POST':
		form = PQRForm(request.POST or None, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/crear_pqr')
	else:
		form = PQRForm()
	return render_to_response('crearPQR.html', locals(), context_instance=RequestContext(request))

@permission_required('contenido.change_pqr', login_url='/ingresar')
def editar_pqr(request, id):
	obj=PQR.objects.get(id=id)
	pqr=PQR.objects.all()
	if request.method=='POST':
		form = PQRForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/crear_pqr')
	else:
		form = PQRForm(instance=obj)
	return render_to_response('crearPQR.html', locals(), context_instance=RequestContext(request))

@permission_required('contenido.delete_documento', login_url='/ingresar')
def eliminar_pqr(request, id):
	modelo="Pregunta/Queja/Reclamo"
	objeto=PQR.objects.get(id=id)
	return render_to_response('eliminarPQR.html', locals(), context_instance=RequestContext(request))

@permission_required('contenido.delete_documento', login_url='/ingresar')
def confirmar_eliminar_pqr(request, id):
	documento=PQR.objects.get(id=id)
	documento.delete()
	return HttpResponseRedirect('/verDocumentos')