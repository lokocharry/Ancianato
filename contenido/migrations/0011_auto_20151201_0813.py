# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0010_auto_20151201_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
    ]
