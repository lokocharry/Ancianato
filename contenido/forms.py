from django import forms
from contenido.models import *
from django.forms.widgets import Textarea

class ContenidoForm(forms.ModelForm):
	class Meta:
		model = Pagina
		fields = '__all__'

class MisionForm(forms.ModelForm):
	class Meta:
		model = Mision
		fields = '__all__'

class HistoriaForm(forms.ModelForm):
	class Meta:
		model = Historia
		fields = '__all__'

class VisionForm(forms.ModelForm):
	class Meta:
		model = Vision
		fields = '__all__'

class DocumentoForm(forms.ModelForm):
	class Meta:
		model = Documento
		fields = '__all__'

class ContactForm(forms.Form):
	nombre = forms.CharField()
	email = forms.EmailField()
	asunto = forms.CharField()
	mensage = forms.CharField(widget=Textarea())
