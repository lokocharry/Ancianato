"""Ancianato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from userena import views as userena_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^$', 'contenido.views.inicio', name='inicio'),
    url(r'^dondeEstamos/', 'contenido.views.dondeEstamos', name='contactenos'),
    url(r'^servicios/', 'contenido.views.servicios', name='servicios'),
    url(r'^subirDocumento/', 'contenido.views.subir_documento', name='subir_documento'),
    url(r'^editarDocumento/(?P<id>\d+)/$', 'contenido.views.editar_documento', name='editar_documento'),
    url(r'^eliminarDocumento/(?P<id>\d+)/$', 'contenido.views.eliminar_documento', name='eliminar_documento'),
    url(r'^confirmarEliminarDocumento/(?P<id>\d+)/$', 'contenido.views.confirmar_eliminar_documento', name='confirmar_eliminar_documento'),
    url(r'^editarConocenos/', 'contenido.views.editar_conocenos', name='editarConocenos'),
    url(r'^crear_pqr/', 'contenido.views.crear_pqr', name='crear_pqr'),
    url(r'^editar_pqr/(?P<id>\d+)/$', 'contenido.views.editar_pqr', name='editar_pqr'),
    url(r'^eliminar_pqr/(?P<id>\d+)/$', 'contenido.views.eliminar_pqr', name='eliminar_pqr'),
    url(r'^confirmar_eliminar_pqr/(?P<id>\d+)/$', 'contenido.views.confirmar_eliminar_pqr', name='confirmar_eliminar_pqr'),
    url(r'^pqr/', 'contenido.views.pqr', name='pqr'),
    url(r'^legalidad/', 'contenido.views.legalidad', name='legalidad'),

    url(r'^conocenos/', 'contenido.views.conocenos', name='conocenos'),
    url(r'^subirLicitacion/', 'contenido.views.subir_licitacion', name='subir_licitacion'),
    url(r'^verDocumentos/', 'contenido.views.verDocumentos', name='verDocumentos'),
    url(r'^verLicitaciones/', 'contenido.views.verLicitaciones', name='verLicitaciones'),

    url(r'^salir', userena_views.signout),
    #url(r'^registrarse/', userena_views.signup),
    url(r'^ingresar/', userena_views.signin),
    url(r'^usuario/', include('userena.urls')),

    url(r'^crear_contenido', 'contenido.views.crear_contenido', name='crear_contenido'),
    url(r'^contactenos/', 'contenido.views.contactenos', name='contactenos'),
    url(r'^ver_contenido/', 'contenido.views.ver_contenido'),
    url(r'^gracias/', 'contenido.views.gracias_contacto', name='contactenos-gracias'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
