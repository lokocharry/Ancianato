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

@permission_required('contenido.add_documento', login_url='/ingresar')
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
		if subject and message and from_email:
			try:
				send_mail(subject, message, from_email, ['jorge.lozano@uptc.edu.co'])
			except BadHeaderError:
				return HttpResponse('Cabecera invalida encontrada.')
			return HttpResponseRedirect('/contactenos/gracias/')
	else:
		return render_to_response('contactenos.html', {'form': ContactForm()}, context_instance=RequestContext(request))

def gracias_contacto(request):
		return render_to_response('gracias.html')

def ver_contenido(request):
	contenido=Pagina.objects.all()
	return render_to_response('verContenido.html', locals(), context_instance=RequestContext(request))

def verDocumentos(request):
	titulo="Últimas Novedades"
	documentos=Documento.objects.filter(tipo="D").order_by('-id')
	return render_to_response('verDocumentos.html', locals(), context_instance=RequestContext(request))

def verLicitaciones(request):
	titulo="Últimas Licitaciones"
	documentos=Documento.objects.filter(tipo="L").order_by('-id')
	return render_to_response('verDocumentos.html', locals(), context_instance=RequestContext(request))