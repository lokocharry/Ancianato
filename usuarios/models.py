from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from userena.models import UserenaBaseProfile

class Usuario(UserenaBaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    documento = models.CharField(max_length=10)
    #NIT