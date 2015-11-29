from django.contrib import admin
from solo.admin import SingletonModelAdmin
from contenido.models import *

# Register your models here.
admin.site.register(Pagina)
admin.site.register(Documento)
admin.site.register(Mision, SingletonModelAdmin)
admin.site.register(Vision, SingletonModelAdmin)
admin.site.register(Historia, SingletonModelAdmin)
