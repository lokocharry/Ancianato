# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0011_auto_20151201_0813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'permissions': (('add_licitacion', 'Can add licitacion'), ('change_licitacion', 'Can change licitacion'), ('delete_licitacion', 'Can delete licitacion'))},
        ),
    ]
