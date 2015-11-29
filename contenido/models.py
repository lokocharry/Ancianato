# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse_lazy
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from solo.models import SingletonModel
import os

class Mision(SingletonModel):
	mision = RichTextUploadingField()

	def __unicode__(self):
		return u"Misión"

	class Meta:
		verbose_name = "Misión"

class Vision(SingletonModel):
	vision = RichTextUploadingField()

	def __unicode__(self):
		return u"Visión"

	class Meta:
		verbose_name = "Visión"

class Historia(SingletonModel):
	historia = RichTextUploadingField()

	def __unicode__(self):
		return u"Historia"

	class Meta:
		verbose_name = "Historia"

class Pagina(models.Model):
    contenido = RichTextUploadingField()

TIPO_DOCUMENTO = (
    ('L', 'Licitación'),
    ('D', 'Documento'),
)

class Documento(models.Model):
	documento = models.FileField(upload_to='documentos/%Y/%m/%d')
	usuario = models.ForeignKey(User, null=True, blank=True)
	tipo=models.CharField(max_length=1, null=True, blank=True, choices=TIPO_DOCUMENTO)

	@property
	def nombre(self):
		return os.path.basename(self.documento.name)

	@property
	def extension(self):
		nombre, extension = os.path.splitext(self.documento.name)
		return extension.replace(".", "")

	def __unicode__(self):
		return self.nombre