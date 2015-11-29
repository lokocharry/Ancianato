from userena.signals import signup_complete
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

def usuario_registrado(sender, **kwargs):
	user = kwargs['user']
	grupo=Group.objects.get_or_create(name="Licitantes")
	perm = Permission.objects.get(codename='add_documento')
	grupo[0].permissions.add(perm)
	perm = Permission.objects.get(codename='change_documento')
	grupo[0].permissions.add(perm)
	perm = Permission.objects.get(codename='delete_documento')
	grupo[0].user_set.add(user)
	print "Usuario registrado agregado al grupo Licitantes"

signup_complete.connect(usuario_registrado)